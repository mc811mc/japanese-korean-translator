import pykakasi
import re
from googletrans import Translator

class JapaneseToKoreanConverter:
    def __init__(self):
        # Initialize KAKASI for Kanji to Hiragana conversion
        self.kakasi = pykakasi.kakasi()
        self.kakasi.setMode('J', 'H')  # Kanji to Hiragana
        self.kakasi.setMode('K', 'H')  # Katakana to Hiragana
        self.converter = self.kakasi.getConverter()

        self.translator = Translator()

        # Romanji to Hangul pronunciation mapping
        self.romanji_to_hangul = {
            'a': '아', 'i': '이', 'u': '우', 'e': '에', 'o': '오',
            'ka': '카', 'ki': '키', 'ku': '쿠', 'ke': '케', 'ko': '코',
            'kya': '키아', 'kyu': '키우', 'kyo': '키요',
            'sa': '사', 'shi': '시', 'su': '스', 'se': '세', 'so': '소',
            'sha': '샤', 'shu': '슈', 'sho': '쇼',
            'ta': '타', 'chi': '치', 'tsu': '츠', 'te': '테', 'to': '토',
            'cha': '차', 'chu': '추', 'cho': '초',
            'na': '나', 'ni': '니', 'nu': '누', 'ne': '네', 'no': '노',
            'nya': '냐', 'nyu': '뉴', 'nyo': '뇨',
            'ha': '하', 'hi': '히', 'fu': '후', 'he': '헤', 'ho': '호',
            'hya': '햐', 'hyu': '휴', 'hyo': '효',
            'ma': '마', 'mi': '미', 'mu': '무', 'me': '메', 'mo': '모',
            'mya': '먀', 'myu': '뮤', 'myo': '묘',
            'ra': '라', 'ri': '리', 'ru': '루', 're': '레', 'ro': '로',
            'rya': '랴', 'ryu': '류', 'ryo': '료',
            'ya': '야', 'yu': '유', 'yo': '요',
            'wa': '와', 'wo': '워', 'wi': '위', 'we': '웨',
            'n': '은',
            'ga': '가', 'gi': '기', 'gu': '구', 'ge': '게', 'go': '고',
            'za': '자', 'ji': '지', 'zu': '즈', 'ze': '제', 'zo': '조',
            'da': '다', 'de': '데', 'do': '도',
            'ba': '바', 'bi': '비', 'bu': '부', 'be': '베', 'bo': '보',
            'pa': '파', 'pi': '피', 'pu': '푸', 'pe': '페', 'po': '포'
        }

    def convert_to_hiragana(self, text: str) -> str:
        return self.converter.do(text)

    def convert_hiragana_to_romanji(self, text: str) -> str:
        romanji_text = ''
        i = 0
        while i < len(text):
            found_combination = False
            for length in range(3, 1, -1):
                if i + length <= len(text):
                    combination = text[i:i+length]
                    if combination in self.romanji_to_hangul:
                        romanji_text += combination
                        i += length
                        found_combination = True
                        break
            if not found_combination:
                romanji_text += text[i]
                i += 1
        return romanji_text

    def convert_romanji_to_hangul(self, romanji: str) -> str:
        hangul_text = ''
        i = 0
        while i < len(romanji):
            found_combination = False
            for length in range(3, 1, -1):
                if i + length <= len(romanji):
                    combination = romanji[i:i+length]
                    if combination in self.romanji_to_hangul:
                        hangul_text += self.romanji_to_hangul[combination]
                        i += length
                        found_combination = True
                        break
            if not found_combination:
                hangul_text += romanji[i]
                i += 1
        # Output is Korean Hangul
        return hangul_text

    def translate_to_korean(self, text: str) -> str:
        try:
            translation = self.translator.translate(text, src='ja', dest='ko')
            return translation.text
        except Exception as e:
            return f"Translation error: {e}"

    def process_japanese_text(self, text: str) -> list:
        results = []
        lines = text.splitlines()  # Split text into lines
        for line in lines:
            if not line.strip():  # Skip empty lines
                continue
            hiragana_text = self.convert_to_hiragana(line)
            romanji_text = self.convert_hiragana_to_romanji(hiragana_text)
            hangul_pronunciation = self.convert_romanji_to_hangul(romanji_text)
            translation = self.translate_to_korean(line)
            results.append({
                'original': line,
                'hangul_pronunciation': hangul_pronunciation,
                'translation': translation
            })
        return results

def main():
    converter = JapaneseToKoreanConverter()

    while True:
        print("\n===== Japanese Text Converter =====")
        print("Enter 'q' to quit")
        text = input("Enter Japanese text to convert: ").strip()

        if text.lower() == 'q':
            print("Exiting the converter. Goodbye!")
            break

        if not text:
            print("Please enter some text.")
            continue

        try:
            results = converter.process_japanese_text(text)
            print("\n--- Conversion Results ---")
            for result in results:
                print(result['original'])
                print(result['hangul_pronunciation'])
                print(result['translation'])
                print()  # Add a blank line between each result

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()