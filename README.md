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

**메소드 기능**</br>
(1) morphs : 형태소 추출</br>
(2) pos : 품사 태깅(Part-of-speech tagging)</br>
(3) nouns : 명사 추출</br>


### 표제어 추출 NLTK WordNetLemmatizer
표제어 추출은 어간 추출과는 달리 단어의 형태가 적절히 보존됨</br>
적절치 못한 단어를 출력하는데, 품사 정보를 알아야만 정확한 결과를 얻을 수 있음</br>
n.lemmatize('dies', 'v')</br>
'die'</br>


### 어간 추출 Porter Algorithm vs. Lancaster Algoritm
s = PorterStemmer()</br>
s.stem(word)</br>

l = LancasterStemmer()</br>
l.stem(word)</br>
**코퍼스에 스태머를 적용하고 어떤 스태머가 해당 코퍼스에 적합한지 판단한 후에 사용하여야 함**  



### 정규 표현식 문법  
정규 표현식을 위해 사용되는 문법 중 특수 문자들은 아래와 같습니다.

**특수 문자	설명**  
.	한 개의 임의의 문자를 나타냅니다. (줄바꿈 문자인 \n는 제외)  
?	앞의 문자가 존재할 수도 있고, 존재하지 않을 수도 있습니다. (문자가 0개 또는 1개)  
\*	앞의 문자가 무한개로 존재할 수도 있고, 존재하지 않을 수도 있습니다. (문자가 0개 이상)  
\+	앞의 문자가 최소 한 개 이상 존재합니다. (문자가 1개 이상)  
^	뒤의 문자로 문자열이 시작됩니다.  
$	앞의 문자로 문자열이 끝납니다.  
{숫자}	숫자만큼 반복합니다.  
{숫자1, 숫자2}	숫자1 이상 숫자2 이하만큼 반복합니다. ?, *, +를 이것으로 대체할 수 있습니다.  
{숫자,}	숫자 이상만큼 반복합니다.  
[ ]	대괄호 안의 문자들 중 한 개의 문자와 매치합니다. [amk]라고 한다면 a 또는 m 또는 k 중 하나라도 존재하면 매치를 의미합니다. [a-z]와 같이 범위를 지정할 수도 있습니다. [a-zA-Z]는 알파벳 전체를 의미하는 범위이며, 문자열에 알파벳이 존재하면 매치를 의미합니다.  
[^문자]	해당 문자를 제외한 문자를 매치합니다.  
l	AlB와 같이 쓰이며 A 또는 B의 의미를 가집니다.  
정규 표현식 문법에는 역 슬래쉬(\)를 이용하여 자주 쓰이는 문자 규칙들이 있습니다.  

**문자 규칙	설명**  
\\	역 슬래쉬 문자 자체를 의미합니다  
\d	모든 숫자를 의미합니다. [0-9]와 의미가 동일합니다.  
\D	숫자를 제외한 모든 문자를 의미합니다. [^0-9]와 의미가 동일합니다.  
\s	공백을 의미합니다. [ \t\n\r\f\v]와 의미가 동일합니다.  
\S	공백을 제외한 문자를 의미합니다. [^ \t\n\r\f\v]와 의미가 동일합니다.  
\w	문자 또는 숫자를 의미합니다. [a-zA-Z0-9]와 의미가 동일합니다.  
\W	문자 또는 숫자가 아닌 문자를 의미합니다. [^a-zA-Z0-9]와 의미가 동일합니다.  


### 정규표현식 모듈 함수  
정규표현식 모듈에서 지원하는 함수는 이와 같습니다.  

**모듈 함수	설명**  
re.compile()	정규표현식을 컴파일하는 함수입니다. 다시 말해, 파이썬에게 전해주는 역할을 합니다. 찾고자 하는 패턴이 빈번한 경우에는 미리 컴파일해놓고 사용하면 속도와 편의성면에서 유리합니다.  
re.search()	문자열 전체에 대해서 정규표현식과 매치되는지를 검색합니다.  
re.match()	문자열의 처음이 정규표현식과 매치되는지를 검색합니다.  
re.split()	정규 표현식을 기준으로 문자열을 분리하여 리스트로 리턴합니다.  
re.findall()	문자열에서 정규 표현식과 매치되는 모든 경우의 문자열을 찾아서 리스트로 리턴합니다. 만약, 매치되는 문자열이 없다면 빈 리스트가 리턴됩니다.  
re.finditer()	문자열에서 정규 표현식과 매치되는 모든 경우의 문자열에 대한 이터레이터 객체를 리턴합니다.  
re.sub()	문자열에서 정규 표현식과 일치하는 부분에 대해서 다른 문자열로 대체합니다.  
