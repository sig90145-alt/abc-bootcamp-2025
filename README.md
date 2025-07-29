# 데이터 부트캠프 실습

이 프로젝트는 데이터 부트캠프 실습용으로, 다양한 파이썬 예제와 실습 코드, 웹앱, AI 활용 예시를 포함합니다.  
Python 3.13 (Anaconda 환경)에서 동작합니다.

## 주요 파일 및 역할

- **01-cil.py**  
  - 파이썬 기본 실행 예제(Hello Python 출력)
- **02-cil.py**  
  - OpenAI API를 활용한 간단한 프롬프트 예제
- **03-cli.py**  
  - 사용자 입력을 받아 AI 관상 분석 결과를 출력하는 CLI 프로그램
- **04-webapp.py**  
  - Streamlit 기반의 AI 관상 분석 웹앱
- **05-cli-streaming.py**  
  - OpenAI API의 스트리밍 응답을 CLI에서 출력하는 예제
- **06-cli-chat.py**  
  - (부분 구현) OpenAI API를 활용한 대화형 챗봇 CLI 예제
- **07-json.py**  
  - Melon 차트 데이터를 JSON으로 받아와 파싱 및 출력하는 예제
- **08-webapp-melon-top100.py**  
  - Melon Top100 데이터를 웹에서 시각화하는 Streamlit 웹앱
- **09-melon-search.py**  
  - Melon 검색 API를 활용한 곡 검색 예제
- **ai.py**  
  - OpenAI API를 활용한 관상 분석 함수 정의
- **audio.py**  
  - gTTS와 pygame을 활용한 음성 합성 및 재생 함수
- **generator_01.py**  
  - 파이썬 제너레이터(generator) 예제

## 실행 방법

1. Python 3.13 (Anaconda) 환경에서 아래 명령어로 필요한 패키지를 설치하세요.
   ```
   pip install -r requirements.txt
   ```
2. 각 예제는 아래와 같이 실행할 수 있습니다.
   ```
   python 01-cil.py
   python 03-cli.py
   streamlit run 04-webapp.py
   ```

## 필요 패키지

- openai
- python-dotenv
- streamlit
- gtts
- pygame
- requests
- httpx

(자세한 버전은 requirements.txt 참고)
