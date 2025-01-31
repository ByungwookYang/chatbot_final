import streamlit as st


def get_current_tool_message(tool_args, tool_call_id):

    if tool_call_id:
        for tool_arg in tool_args:
            if tool_arg["tool_call_id"] == tool_call_id:
                return tool_arg
        return None
    else:
        return None


def format_search_result(results):

    import json

    results = json.loads(results)

    answer = ""
    for result in results:
        answer += f'**[{result["title"]}]({result["url"]})**\n\n'
        answer += f'{result["content"]}\n\n'
        answer += f'신뢰도: {result["score"]}\n\n'
        answer += "\n-----\n"
    return answer


def format_pdf_search_result(results):
    import re

    documents = re.findall(
        r"<document><context>(.*?)</context><metadata><source>(.*?)</source><page>(\d+)</page></metadata></document>",
        results,
        re.DOTALL,
    )

    answer = ""
    for context, source, page in documents:
        answer += f"출처: {source} (페이지 {page})\n"
        answer += "\n\n"
        answer += f"내용: {context.strip()}\n"
        answer += "\n-----\n"

    return answer.strip()  # 마지막 줄바꿈 제거


# used
def stream_handler(streamlit_container, agent_executor, inputs, config):
    # Initialize result storage
    tool_args = []
    agent_answer = ""
    agent_message = None  # Pre-declare agent_message variable

    container = streamlit_container.container()
    with container:
        for chunk_msg, metadata in agent_executor.stream(
            inputs, config, stream_mode="messages"
        ):
            if hasattr(chunk_msg, "tool_calls") and chunk_msg.tool_calls:
                # Initialize tool call result
                tool_arg = {
                    "tool_name": "",
                    "tool_result": "",
                    "tool_call_id": chunk_msg.tool_calls[0]["id"],
                }
                # Save tool name
                tool_arg["tool_name"] = chunk_msg.tool_calls[0]["name"]
                if tool_arg["tool_name"]:
                    tool_args.append(tool_arg)

            if hasattr(chunk_msg, "tool_call_chunks") and chunk_msg.tool_call_chunks:
                if len(chunk_msg.tool_call_chunks) > 0:  # Add None check
                    # Accumulate tool call arguments
                    chunk_msg.tool_call_chunks[0]["args"]

            if metadata["langgraph_node"] == "tools":
                # Save tool execution results
                current_tool_message = get_current_tool_message(
                    tool_args, chunk_msg.tool_call_id
                )
                if current_tool_message:
                    current_tool_message["tool_result"] = chunk_msg.content
                    with st.status(f'✅ {current_tool_message["tool_name"]}'):
                        if current_tool_message["tool_name"] == "web_search":
                            st.markdown(
                                format_search_result(
                                    current_tool_message["tool_result"]
                                )
                            )
                        elif current_tool_message["tool_name"] == "pdf_retriever":
                            st.markdown(
                                format_pdf_search_result(
                                    current_tool_message["tool_result"]
                                )
                            )

            if metadata["langgraph_node"] == "agent":
                if chunk_msg.content:
                    if agent_message is None:
                        agent_message = st.empty()
                    # Accumulate agent message
                    agent_answer += chunk_msg.content
                    agent_message.markdown(agent_answer)

        return container, tool_args, agent_answer
