# 프로젝트 소개
- 개인 맞춤형 상담 봇으로, 개인정보를 입력하면 해당 정보에 부합하는 상담봇 페르소나가 지정됩니다.
- 일반적으로 공감과 위로를 얻을 수 있는 챗봇이고, pdf retriever, web search tool을 이용해 정보를 얻을 수도 있습니다.
- pdf파일을 원하는 파일로 바꾸려면 data폴더 내에 파일을 변경하고, modules/bk_tools.py로 들어가 파일 이름을 변경해주시면 됩니다.
- 다른 tool을 추가하기 위해서는 sidebar.py 부분에서 다른 tool을 추가하고, modules/agent.py부분에서 프롬프트를 수정해 사용하실 수 있습니다.
- 챗봇 사용 링크 : https://chatbot-for-survey.streamlit.app/

![Uploading image.png…]()

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


