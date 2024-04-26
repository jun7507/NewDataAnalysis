# 특정 키워드로 검색한 네이버 뉴스(news.naver.com)의 기사 제목을 크롤링하여 간단한 텍스트 분석을 수행하는 프로그램을 작성하시오.
# 필요한 기능은 다음과 같다.
# 1. 원하는 뉴스 기사 데이터를 받아오는 기능( 텍스트 수집 기능) crolling.py
# 2. 뉴스 기사 빈도 분석하는 기능( 각 단어의 빈도를 계산) analysis.py
# 3. 빈도 히스토그램, wordcloud를 출력하는 기능 (시각화를 통한 분석) visualization.py
# 4. 생성한 뉴스 데이터를 Elastic Search를 사용하여 저장하는 기능 (데이터 저장 기능) elasticsearch.py
# 5. Elastic Search에 저장된 데이터를 검색하는 기능 (데이터 검색 기능) elasticsearch.py
# 6. 위의 기능을 모두 실행하는 main.py(프로그램의 실행)

from crolling import NewsCrawler
from analysis import TextAnalyzer
from visualization import Visualizer
from es_manager import ElasticsearchManager

def main():
    keyword = input("Enter the keyword for news search: ")
    crawler = NewsCrawler()
    titles = crawler.crawl_news_titles(keyword)

    if not titles:
        print("No titles found for the keyword.")
        return

    analyzer = TextAnalyzer()
    frequencies = analyzer.analyze_frequency(titles)

    visualizer = Visualizer()
    visualizer.plot_histogram(frequencies)
    visualizer.generate_wordcloud(frequencies)

    es_manager = ElasticsearchManager()
    documents = [{'text': title} for title in titles]
    saved_results = es_manager.save_to_elasticsearch(documents)
    print("Data has been saved to Elasticsearch. Saved documents:")
    for _id, text in saved_results:
        print(f"Document ID: {_id}, Text: {text[:50]}...")

    search_results = es_manager.search_in_elasticsearch(keyword)
    print("Search results from Elasticsearch:")
    for result in search_results:
        print(result['_source']['text'])

if __name__ == "__main__":
    main()



