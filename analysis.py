import html
from collections import Counter

class TextAnalyzer:
    def analyze_frequency(self, titles):
        words = []
        for title in titles:
            title = html.unescape(title)  # HTML 엔티티 디코드
            words.extend(title.split()) # 단어 단위로 분할
        return Counter(words)


