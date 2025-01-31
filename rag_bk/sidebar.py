import streamlit as st
from langchain_core.prompts import load_prompt, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from rag_bk.modules.bk_tools import WebSearchTool, retriever_tool
from rag_bk.modules.agent import create_agent_executor
from rag_bk.bk_messages import random_uuid


# 사이드바 배치 함수화
def show_sidebar():
    with st.sidebar:
        # 초기화 버튼
        clear_btn = st.button("대화 초기화")

        st.subheader("간단한 개인정보를 입력해주세요.")

        # 나이 입력
        age_val = st.number_input(
            "나이",
            min_value=0,
            max_value=120,
            value=0,
        )

        # 성별 입력
        gender_val = st.selectbox(
            "성별",
            ("남자", "여자"),
            index=None,
            placeholder="성별을 선택하세요...",
        )

        # 결혼 여부
        married_val = st.radio(
            "기혼여부",
            ["기혼💍", "미혼👨🏻‍💻", "재혼💛", "기타"],
            index=None,
        )

        # 자녀 정보
        options_val = st.multiselect(
            "자녀정보",
            [
                "없음",
                "아들",
                "딸",
                "1명",
                "2명",
                "3명",
                "0-5세",
                "6-10세",
                "11-15세",
                "16-20세",
                "20세 이상",
            ],
            default=None,
        )

        # 가족과의 유대감 점수
        family_score_val = st.slider(
            "가족과의 유대감 점수",
            min_value=0,
            max_value=10,
            step=1,
        )

        # 추가 상담 요청 내용
        user_text_prompt = st.text_area(
            "상담 요청 내용",
            "폐암에 대한 상담 요청",
            height=100,
        )

        # 제출 버튼
        apply_btn = st.button("제출", key="primary")

        # 제출 버튼을 누르면..
        if apply_btn:
            with st.spinner("챗봇상담사를 지정중입니다..."):  # spinner가 생성되면서..
                # step 1 LLM을 통한 페르소나를 부여 프롬프트 생성하기
                # gen_prom.yaml 로드(개인정보에 맞는 페르소나를 부여하기 위한 프롬프트)
                loaded_prompt = load_prompt("prompts/gen_prom.yaml", encoding="utf-8")

                # 최종 페르소나 부여 프롬프트 생성(상담자 답변 읽어오기)
                final_template = f"""
                    상담을 원하는 내용은 {user_text_prompt}, 
                    사용자의 나이는 {age_val}, 성별은 {gender_val}, 
                    결혼여부는 {married_val}, 자녀정보는 {options_val}, 
                    가족과의 유대감점수는 10점 만점에 {family_score_val},
                    {loaded_prompt.template}
                    """

                # 페르소나 생성 LLM 호출 (첫 번째 체인)
                prompt1 = PromptTemplate.from_template(template=final_template)
                llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
                chain1 = prompt1 | llm | StrOutputParser()
                st.session_state["new_prompt"] = chain1.invoke(
                    ""
                )  # 생성된 페르소나 저장

                # step 2 생성된 페르소나를 이용한 최종 답변 LLM 생성
                tool1 = retriever_tool()  # pdf_search

                # WebSearchTool 인스턴스 생성
                tool2 = WebSearchTool().create()  # web_search

                # 리액트형 에이전트 생성
                st.session_state["react_agent"] = create_agent_executor(
                    model_name="gpt-4o-mini",
                    tools=[tool1, tool2],
                )
                # 고유 스레드 ID(랜덤으로 지어주기 -> 대화 기억용도 -> 대화내용 초기화하면 이것도 초기화)
                st.session_state["thread_id"] = random_uuid()

                st.success("제출이 완료되었습니다! 상담을 진행하세요.")

    # 초기화 버튼이 눌리면...
    if clear_btn:
        st.session_state["messages"] = []  # 대화 정보 지우기
        st.session_state["thread_id"] = random_uuid()  # 사용자정보 기억 지우기
