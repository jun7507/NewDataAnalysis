import os
import urllib.request
from urllib.parse import quote
from dotenv import load_dotenv

class NewsCrawler:
    def __init__(self):
        load_dotenv()  # 환경 변수 파일 로드
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')

    def crawl_news_titles(self, keyword):
        enc_text = quote(keyword)
        url = f"https://openapi.naver.com/v1/search/news?query={enc_text}"  # 뉴스 검색 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)
        
        with urllib.request.urlopen(request) as response:
            rescode = response.getcode()
            if rescode == 200:
                response_body = response.read()
                titles = self.parse_titles(response_body.decode('utf-8'))
                return titles
            else:
                print(f"Error Code: {rescode}")
                return []

    def parse_titles(self, json_str):
        import json
        result = json.loads(json_str)
        titles = [item['title'] for item in result['items']]
        return titles
