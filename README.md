# 프로젝트 이름: News Analysis with Elasticsearch

## 프로젝트 개요
이 프로젝트는 네이버 뉴스에서 특정 키워드로 검색한 기사 제목을 크롤링하여, 간단한 텍스트 분석을 수행하고 결과를 Elasticsearch에 저장하며 검색할 수 있는 기능을 제공합니다. 사용자는 뉴스 기사 데이터를 수집, 분석하고, 시각화를 통해 인사이트를 얻을 수 있습니다.

## 기능
- **데이터 수집**: 특정 키워드에 대한 네이버 뉴스 타이틀을 크롤링합니다.
- **데이터 분석**: 수집된 데이터에서 단어 빈도를 계산합니다.
- **데이터 시각화**: 빈도 분석 결과를 바탕으로 히스토그램과 워드 클라우드를 생성합니다.
- **데이터 저장 및 검색**: 분석된 데이터를 Elasticsearch에 저장하고, 저장된 데이터를 검색할 수 있습니다.

## 설치 방법
### 필요 조건
- Python 3.8 이상
- Elasticsearch 7.x
- 필요한 Python 패키지: `requests`, `beautifulsoup4`, `matplotlib`, `wordcloud`, `elasticsearch`

### 설치 절차
1. 이 저장소를 클론합니다.
   ```bash
   git clone https://your-repository-url.git
   ```
2. 필요한 패키지를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```
3. Elasticsearch를 로컬 머신에 설치하고 실행합니다. [Elasticsearch 설치 가이드](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)를 참조하세요.

## 사용 방법
1. `main.py` 파일을 실행합니다.
   ```bash
   python main.py
   ```
2. 프롬프트에 검색할 키워드를 입력합니다.
3. 프로그램이 데이터를 수집, 분석, 시각화하고 Elasticsearch에 저장합니다.

![Figure_1](https://github.com/jun7507/NewDataAnalysis/assets/92439723/ed8964d4-a8a2-420f-a8f5-e6f6b289134d)
![Figure2_1](https://github.com/jun7507/NewDataAnalysis/assets/92439723/11d104c2-98c3-4037-ac43-66fcd083f40d)
![203954](https://github.com/jun7507/NewDataAnalysis/assets/92439723/3fee0456-131f-4ecc-a547-dc79d9a85109)

## 구성 파일 설명
- **crolling.py**: 키워드에 따른 뉴스 크롤링을 담당합니다.
- **analysis.py**: 수집된 데이터의 빈도 분석을 처리합니다.
- **visualization.py**: 데이터 시각화 기능을 구현합니다.
- **elasticsearch.py**: Elasticsearch와의 데이터 저장 및 검색 기능을 담당합니다.
- **main.py**: 프로그램의 메인 실행 파일입니다.


## 문제 해결
만약 Elasticsearch 연결에 문제가 생긴 경우, Elasticsearch 서버 설정을 확인하고 서버가 실행 중인지 확인하세요. 또한, 방화벽 설정이 Elasticsearch 서버 포트를 차단하고 있지 않은지 검사하세요.
