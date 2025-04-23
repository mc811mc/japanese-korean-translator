from googletrans import Translator
from pykakasi import kakasi

class JapaneseToKoreanConverter:
    def __init__(self):
        self.translator = Translator()
        # Initialize kakasi for Japanese text processing
        self.kakasi = kakasi()
        self.kakasi.setMode('J', 'H')  # Kanji to Hiragana
        self.kakasi.setMode('K', 'H')  # Katakana to Hiragana
        self.converter = self.kakasi.getConverter()

    def convert_to_yomikata(self, text):
        """Convert Japanese text to Korean pronunciation"""
        # Convert to hiragana first
        hiragana = self.converter.do(text)
        
        # Convert hiragana to Korean pronunciation
        # Basic mapping for common sounds
        mapping = {
            # Basic vowels
            'あ': '아', 'い': '이', 'う': '우', 'え': '에', 'お': '오',
            'ア': '아', 'イ': '이', 'ウ': '우', 'エ': '에', 'オ': '오',
            
            # K series
            'か': '카', 'き': '키', 'く': '쿠', 'け': '케', 'こ': '코',
            'カ': '카', 'キ': '키', 'ク': '쿠', 'ケ': '케', 'コ': '코',
            'が': '가', 'ぎ': '기', 'ぐ': '구', 'げ': '게', 'ご': '고',
            'ガ': '가', 'ギ': '기', 'グ': '구', 'ゲ': '게', 'ゴ': '고',
            
            # S series
            'さ': '사', 'し': '시', 'す': '스', 'せ': '세', 'そ': '소',
            'サ': '사', 'シ': '시', 'ス': '스', 'セ': '세', 'ソ': '소',
            'ざ': '자', 'じ': '지', 'ず': '즈', 'ぜ': '제', 'ぞ': '조',
            'ザ': '자', 'ジ': '지', 'ズ': '즈', 'ゼ': '제', 'ゾ': '조',
            
            # T series
            'た': '타', 'ち': '치', 'つ': '츠', 'て': '테', 'と': '토',
            'タ': '타', 'チ': '치', 'ツ': '츠', 'テ': '테', 'ト': '토',
            'だ': '다', 'ぢ': '지', 'づ': '즈', 'で': '데', 'ど': '도',
            'ダ': '다', 'ヂ': '지', 'ヅ': '즈', 'デ': '데', 'ド': '도',
            
            # N series
            'な': '나', 'に': '니', 'ぬ': '누', 'ね': '네', 'の': '노',
            'ナ': '나', 'ニ': '니', 'ヌ': '누', 'ネ': '네', 'ノ': '노',
            
            # H series
            'は': '하', 'ひ': '히', 'ふ': '후', 'へ': '헤', 'ほ': '호',
            'ハ': '하', 'ヒ': '히', 'フ': '후', 'ヘ': '헤', 'ホ': '호',
            'ば': '바', 'び': '비', 'ぶ': '부', 'べ': '베', 'ぼ': '보',
            'バ': '바', 'ビ': '비', 'ブ': '부', 'ベ': '베', 'ボ': '보',
            'ぱ': '파', 'ぴ': '피', 'ぷ': '푸', 'ぺ': '페', 'ぽ': '포',
            'パ': '파', 'ピ': '피', 'プ': '푸', 'ペ': '페', 'ポ': '포',
            
            # M series
            'ま': '마', 'み': '미', 'む': '무', 'め': '메', 'も': '모',
            'マ': '마', 'ミ': '미', 'ム': '무', 'メ': '메', 'モ': '모',
            
            # Y series
            'や': '야', 'ゆ': '유', 'よ': '요',
            'ヤ': '야', 'ユ': '유', 'ヨ': '요',
            
            # R series
            'ら': '라', 'り': '리', 'る': '루', 'れ': '레', 'ろ': '로',
            'ラ': '라', 'リ': '리', 'ル': '루', 'レ': '레', 'ロ': '로',
            
            # W series
            'わ': '와', 'を': '오', 'ん': '은',
            'ワ': '와', 'ヲ': '오', 'ン': '은',
            
            # Small characters
            'ぁ': '아', 'ぃ': '이', 'ぅ': '우', 'ぇ': '에', 'ぉ': '오',
            'ァ': '아', 'ィ': '이', 'ゥ': '우', 'ェ': '에', 'ォ': '오',
            'っ': '', 'ッ': '',
            
            # Special combinations
            'きゃ': '캬', 'きゅ': '큐', 'きょ': '쿄',
            'キャ': '캬', 'キュ': '큐', 'キョ': '쿄',
            'ぎゃ': '갸', 'ぎゅ': '규', 'ぎょ': '교',
            'ギャ': '갸', 'ギュ': '규', 'ギョ': '교',
            
            'しゃ': '샤', 'しゅ': '슈', 'しょ': '쇼',
            'シャ': '샤', 'シュ': '슈', 'ショ': '쇼',
            'じゃ': '자', 'じゅ': '주', 'じょ': '조',
            'ジャ': '자', 'ジュ': '주', 'ジョ': '조',
            
            'ちゃ': '차', 'ちゅ': '추', 'ちょ': '초',
            'チャ': '차', 'チュ': '추', 'チョ': '초',
            
            'にゃ': '냐', 'にゅ': '뉴', 'にょ': '뇨',
            'ニャ': '냐', 'ニュ': '뉴', 'ニョ': '뇨',
            
            'ひゃ': '햐', 'ひゅ': '휴', 'ひょ': '효',
            'ヒャ': '햐', 'ヒュ': '휴', 'ヒョ': '효',
            'びゃ': '뱌', 'びゅ': '뷰', 'びょ': '뵤',
            'ビャ': '뱌', 'ビュ': '뷰', 'ビョ': '뵤',
            'ぴゃ': '퍄', 'ぴゅ': '퓨', 'ぴょ': '표',
            'ピャ': '퍄', 'ピュ': '퓨', 'ピョ': '표',
            
            'みゃ': '먀', 'みゅ': '뮤', 'みょ': '묘',
            'ミャ': '먀', 'ミュ': '뮤', 'ミョ': '묘',
            
            'りゃ': '랴', 'りゅ': '류', 'りょ': '료',
            'リャ': '랴', 'リュ': '류', 'リョ': '료',
            
            # Special katakana combinations
            'ファ': '파', 'フィ': '피', 'フェ': '페', 'フォ': '포',
            'ウィ': '위', 'ウェ': '웨', 'ウォ': '워',
            'ヴァ': '바', 'ヴィ': '비', 'ヴ': '부', 'ヴェ': '베', 'ヴォ': '보',
            'ティ': '티', 'ディ': '디',
            'トゥ': '투', 'ドゥ': '두',
            'チェ': '체', 'ジェ': '제',
            'シェ': '셰', 'ジェ': '제',
            'イェ': '예',
            'クァ': '콰', 'クィ': '퀴', 'クェ': '퀘', 'クォ': '쿼',
            'グァ': '과', 'グィ': '귀', 'グェ': '궤', 'グォ': '궈',
            
            # Punctuation and special characters
            'ー': '-',  # Prolonged sound mark
            '、': ', ',  # Comma
            '。': '. ',  # Period
            '！': '! ',  # Exclamation mark
            '？': '? ',  # Question mark
            '「': '"',  # Opening quote
            '」': '"',  # Closing quote
            '『': '"',  # Opening double quote
            '』': '"',  # Closing double quote
        }

        result = ''
        i = 0
        while i < len(hiragana):
            # Check for 3-character combinations first (special cases)
            if i + 2 < len(hiragana):
                trigraph = hiragana[i:i+3]
                if trigraph in mapping:
                    result += mapping[trigraph]
                    i += 3
                    continue

            # Check for 2-character combinations
            if i + 1 < len(hiragana):
                digraph = hiragana[i:i+2]
                if digraph in mapping:
                    result += mapping[digraph]
                    i += 2
                    continue

            # Then check single characters
            char = hiragana[i]
            if char in mapping:
                result += mapping[char]
            else:
                result += char
            i += 1

        return result

    def process_japanese_text(self, text):
        """Process Japanese text and return conversion results"""
        results = []
        lines = text.splitlines()
        
        for line in lines:
            if not line.strip():
                continue

            try:
                # Get yomikata (Korean pronunciation)
                yomikata = self.convert_to_yomikata(line)
                
                # Get translation
                translation = self.translator.translate(line, src='ja', dest='ko').text
                
                results.append({
                    'yomikata': yomikata,
                    'original': line,
                    'translation': translation
                })
            except Exception as e:
                print(f"Error processing line '{line}': {str(e)}")
                continue
                
        return results 