import re
from elasticsearch import Elasticsearch

def remove_html_tags(text):
    """HTML 태그를 제거하는 함수"""
    clean_text = re.sub(r'<[^>]+>', '', text)
    return clean_text

class ElasticsearchManager:
    def __init__(self, index_name='news_data'):
        self.es = Elasticsearch(
            ['http://localhost:9200'],
            http_auth=('elastic', '12345678')  # 인증 정보
        )
        self.index_name = index_name

    def save_to_elasticsearch(self, data):
        results = []
        for i, doc in enumerate(data):
            # HTML 태그를 제거
            doc_cleaned = remove_html_tags(doc['text'])
            response = self.es.index(index=self.index_name, id=i+1, document={'text': doc_cleaned})
            results.append((response['_id'], doc_cleaned))
        return results

    def search_in_elasticsearch(self, keyword):
        query = {
            "query": {
                "match": {
                    "text": keyword
                }
            }
        }
        response = self.es.search(index=self.index_name, body=query)
        hits = []
        for hit in response['hits']['hits']:
            # HTML 태그를 제거
            hit_cleaned = hit['_source']['text']
            hit['_source']['text'] = remove_html_tags(hit_cleaned)
            hits.append(hit)
        return hits
