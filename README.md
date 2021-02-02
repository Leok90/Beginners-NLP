# Beginners-NLP
딥 러닝을 이용한 자연어 처리 입문 - 위키독스

### pandas_profiling
데이터베이스의 정보 출력
1. Overview
- Missing cells
- Duplicate rows
- Variable types
2. Variables
3. Correlations by heatmap
4. Missing values
5. Sample
6. Last rows
7. Duplicate rows


### 토큰화 기법 비교(아포스트로피(') 분리)
1. NLTK word_tokenize
Don't를 Do와 n't로 분리</br>
Jone's를 jone과 's로 분리</br>
구두점(.) 분리 x</br>

2. NLTK WordPuncTokenizer
구두점(.)을 별도로 분리</br>
Don't를 Don과 '와 t로 분리</br>
Jone's를 Jone과 '와 s로 분리</br>

3. Keras text_to_word_sequence
모든 알파벳을 소문자로 변경</br>
마침표, 컴마, 느낌표 등의 구두점 제거</br>
don't나 jone's의 아포스트로피(')는 보존</br>


문장 토큰화 오픈 소스 NLTK, OpenNLP, 스탠포드 CoreNLP, splitta, LingPipe</br>
https://www.grammarly.com/blog/engineering/how-to-split-sentences/</br>


### NLTK와 KoNLPy에서 품사 태깅 비교
1. NLTK pos_tag 영어 문장 토큰화 및 품사 태깅

2. KoNLPy(코엔엘파이)
- Okt(Open Korea Text)
- Mecab(메캅)
- Komoran(코모란)
- Hannanum(한나눔)
- Kkma(꼬꼬마)
형태소(morpheme) 단위로 토큰화</br>
** 메소드 기능**
1) morphs : 형태소 추출
