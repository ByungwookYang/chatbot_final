from typing import Any, List
from modules.bk_tavily_tool import TavilySearch
from .base import BaseTool
from modules.bk_pdf_tool import PDFRetrievalChain
from langchain_core.tools.retriever import create_retriever_tool
from langchain_core.prompts import PromptTemplate


# 인터넷 검색 도구 생성
class WebSearchTool(BaseTool[TavilySearch]):
    """웹 검색을 수행하는 도구 클래스"""

    def __init__(
        self,
        topic: str = "general",
        max_results: int = 3,
        include_answer: bool = False,
        include_raw_content: bool = False,
        include_images: bool = False,
        format_output: bool = False,
        include_domains: List[str] = [],
        exclude_domains: List[str] = [],
    ):
        """WebSearchTool 초기화 메서드"""
        super().__init__()
        self.topic = topic
        self.max_results = max_results
        self.include_answer = include_answer
        self.include_raw_content = include_raw_content
        self.include_images = include_images
        self.format_output = format_output
        self.include_domains = include_domains
        self.exclude_domains = exclude_domains

    def _create_tool(self) -> TavilySearch:
        """TavilySearch 객체를 생성하고 설정하는 내부 메서드"""
        search = TavilySearch(
            topic=self.topic,
            max_results=self.max_results,
            include_answer=self.include_answer,
            include_raw_content=self.include_raw_content,
            include_images=self.include_images,
            format_output=self.format_output,
            include_domains=self.include_domains,
            exclude_domains=self.exclude_domains,
        )
        search.name = "web_search"
        search.description = "Use this tool to search on the web"
        return search

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """도구를 실행하는 메서드"""
        tool = self._create_tool()
        return tool(*args, **kwargs)


# PDF 검색 도구 생성
def retriever_tool():
    pdf = PDFRetrievalChain(["data/NCI_lung_removed.pdf"]).create_chain()

    pdf_retriever = pdf.retriever

    retriever_tool = create_retriever_tool(
        pdf_retriever,
        "pdf_retriever",
        "Search and return information about NCI_lung_removed PDF file. It contains useful information on recent AI trends. The document is published on Dec 2023.",
        document_prompt=PromptTemplate.from_template(
            "<document><context>{page_content}</context><metadata><source>{source}</source><page>{page}</page></metadata></document>"
        ),
    )
    return retriever_tool
