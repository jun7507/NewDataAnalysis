# 특정 키워드로 검색한 네이버 뉴스(news.naver.com)의 기사 제목을 크롤링하여 간단한 텍스트 분석을 수행하는 프로그램을 작성하시오.
# 필요한 기능은 다음과 같다.
# 1. 원하는 뉴스 기사 데이터를 받아오는 기능( 텍스트 수집 기능) crolling.py
# 2. 뉴스 기사 빈도 분석하는 기능( 각 단어의 빈도를 계산) analysis.py
# 3. 빈도 히스토그램, wordcloud를 출력하는 기능 (시각화를 통한 분석) visualization.py
# 4. 생성한 뉴스 데이터를 Elastic Search를 사용하여 저장하는 기능 (데이터 저장 기능) elasticsearch.py
# 5. Elastic Search에 저장된 데이터를 검색하는 기능 (데이터 검색 기능) elasticsearch.py
# 6. 위의 기능을 모두 실행하는 main.py(프로그램의 실행)