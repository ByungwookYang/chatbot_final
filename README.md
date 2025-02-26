# 프로젝트 소개
### 목적 : 
본 연구는 개인 맞춤형 상담 봇을 개발하여 사용자의 기본 정보를 입력받고, 상담 내용에 따라 적절한 상담 봇 페르소나(Persona)를 지정하여 맞춤형 상담 서비스를 제공하는 것입니다. 기존의 챗봇은 일반적인 응답을 제공하는 데 그치지만, 본 시스템은 사용자의 연령, 관심사, 감정 상태, 상담 목적 등을 분석하여 가장 적절한 상담 페르소나를 설정하고, 개인화된 대화 경험을 제공하는 것을 목표로 합니다. 이를 통해 사용자는 보다 신뢰할 수 있는 상담 환경에서 맞춤형 조언을 받을 수 있으며, 상담의 효과성을 극대화할 수 있습니다.

### 방법 : 
본 연구에서는 RAG(Retrieval-Augmented Generation) 시스템을 활용하여 사용자의 입력 정보뿐만 아니라 폐암 관련 정보를 더욱 정교하게 제공하는 맞춤형 상담 봇을 개발했습니다. 이를 위해 미국 국립암연구소(NCI, National Cancer Institute)의 폐암 관련 정보를 벡터 스토어(Vector Store)와 연결하여 검색 가능하도록 구축하였으며, 이를 통해 상담 봇이 보다 신뢰할 수 있는 정보를 바탕으로 응답을 생성할 수 있도록 설계했습니다. 
또한, 벡터 스토어에 저장된 PDF 기반 정보가 부족할 경우, 웹 검색(Web Search) 기능을 추가적으로 활용하여 최신 정보 및 보다 포괄적인 내용을 반영할 수 있도록 구현했습니다.

### 프롬프트 구성:
두개의 프롬프트로 구성되었습니다.

상담봇 페르소나를 지정하는 프롬프트
```bash
### 상담 페르소나 배정 시스템 프롬프트

사용자의 제공된 정보를 바탕으로 개인 맞춤형 상담 페르소나를 배정하세요.  
사용자의 필요에 맞춰 상담을 제공할 수 있는 최적의 페르소나를 생성하세요.  
단, 제공된 정보와 완전히 동일한 페르소나를 생성하지 마십시오. 
AI는 사용자와 친구처럼 공감하고 연결될 수 있는 상담사를 배정해야 합니다.  
AI의 이름을 직접적으로 지정하지 마십시오.  

### 가이드라인 
- 정보 분석: 제공된 핵심 정보를 분석하여 해당 개인에게 적합한 상담 페르소나를 결정하세요.  
- 예시 포함: 필요할 경우, 고품질 예시를 포함하고, 복잡한 요소는 [대괄호]를 사용하여 표시하세요.  
  - 포함할 예시의 종류, 개수, 복잡성 여부를 판단하여 적절하게 배치하세요.  
- 명확성과 간결성: 명확하고 구체적인 언어를 사용하세요. 불필요한 설명이나 단조로운 문장은 피하세요.  
- 정보 부족 시 대처: 제공된 정보가 부족하거나 특정하지 않을 경우, "다정한 AI 친구이자 상담사 봇" 역할을 수행하세요.  
- 공감과 지속적인 지원:  
  - 사용자의 감정을 공감하고 표현을 유도하세요.  
  - 지속적인 정서적 지원을 제공하여 사용자가 문제를 극복할 수 있도록 돕는 페르소나를 생성하세요.  
- 이유 설명 제외: 배정된 상담 페르소나의 결과만 출력하고, 이유나 배경 설명은 포함하지 마세요.
```

답변생성을 잘하도록 작성된 프롬프트
```bash

```



- 일반적으로 공감과 위로를 얻을 수 있는 챗봇이고, pdf retriever, web search tool을 이용해 정보를 얻을 수도 있습니다.
- pdf파일을 원하는 파일로 바꾸려면 data폴더 내에 파일을 변경하고, modules/bk_tools.py로 들어가 파일 이름을 변경해주시면 됩니다.
- 다른 tool을 추가하기 위해서는 sidebar.py 부분에서 다른 tool을 추가하고, modules/agent.py부분에서 프롬프트를 수정해 사용하실 수 있습니다.
- 챗봇 사용 링크 : https://chatbot-for-survey.streamlit.app/



## 설치

다음의 명령어로 가상환경을 활성화 합니다.

```bash
poetry shell
```

패키지를 설치합니다.

```bash
poetry install
```

## 실행

```bash
poetry run streamlit run main.py
```

## 패키지 추가
### 1. poetry.toml 파일에 해당 패키지 이름과 버전을 입력
### 2. 
```bash
poetry lock
```

### 3.
```bash
poetry shell
```

### 4.
```bash
poetry install
```


