# 프로젝트 소개
목적 : 본 연구는 개인 맞춤형 상담 봇을 개발하여 사용자의 기본 정보를 입력받고, 상담 내용에 따라 적절한 상담 봇 페르소나(Persona)를 지정하여 맞춤형 상담 서비스를 제공하는 것입니다. 기존의 챗봇은 일반적인 응답을 제공하는 데 그치지만, 본 시스템은 사용자의 연령, 관심사, 감정 상태, 상담 목적 등을 분석하여 가장 적절한 상담 페르소나를 설정하고, 개인화된 대화 경험을 제공하는 것을 목표로 합니다. 이를 통해 사용자는 보다 신뢰할 수 있는 상담 환경에서 맞춤형 조언을 받을 수 있으며, 상담의 효과성을 극대화할 수 있습니다.



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


