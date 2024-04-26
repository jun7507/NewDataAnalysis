import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud
import re  # 정규식을 위한 re 모듈 추가
import html  # HTML 엔티티를 변환하기 위한 html 모듈 추가

# HTML 태그를 제거하는 함수 추가
def remove_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)

plt.style.use('classic')
font_path = "C:/Windows/Fonts/malgun.ttf"  # 맑은 고딕 폰트 경로
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

class Visualizer:
    def plot_histogram(self, frequencies):
        words, counts = zip(*frequencies.most_common(10))
        # HTML 태그를 제거
        words = [remove_html_tags(html.unescape(word)) for word in words]
        plt.figure(figsize=(10, 5))
        plt.bar(words, counts)
        plt.xlabel('단어')
        plt.ylabel('빈도수')
        plt.title('상위 10개 단어 빈도수')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_wordcloud(self, frequencies):
        # HTML 엔티티와 태그를 제거하여 워드 클라우드 생성
        frequencies = {remove_html_tags(html.unescape(word)): count for word, count in frequencies.items()}
        wordcloud = WordCloud(width=800, height=400, font_path=font_path, background_color='white').generate_from_frequencies(frequencies)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
