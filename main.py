import re

# 문자열 내에서 패턴 검색
pattern = re.compile("apple")  # 검색할 패턴
text = "I have an apple and a banana."  # 검색 대상 문자열

match = re.match(pattern, 'apple banana')  #첫 문자열이 패턴과 일치
print(match)
print(type(match))  #Match타입

search = re.search(pattern, text)  # 문자열 내에서 패턴 검색
print(search)  #제일 처음 있는 pattern의 위치 반환

# 패턴에 매칭되는 모든 문자열 찾기
matches = re.findall(pattern, text)  #모든 apple검색
print("찾은 모든 문자열:", matches)
print(type(matches))  #리스트

# 패턴으로 문자열 대체
new_text = re.sub(pattern, "orange", text)  #찾은 모든 apple를 orange로 바꿈
print("대체된 문자열:", new_text)

text2 = 'The Regular a Expresion !!! 123 @#! 한글'

pattern = re.compile('\d+')  # 숫자만, +는 1번 이상 반복 [0-9]
print(pattern.findall(text2))

pattern = re.compile('\D+')  # 숫자가 아닌것, [^0-9]
print(pattern.findall(text2))

pattern = re.compile('\s+')  # 공백 문자만  [ \t\n\r\f\v]
print(pattern.findall(text2))

pattern = re.compile('\S+')  # 공백문자가 아닌것 [^ \t\n\r\f\v]
print(pattern.findall(text2))

pattern = re.compile('\w+')  # 문자+숫자 [a-zA-Z0-9]
print(pattern.findall(text2))

pattern = re.compile('\W+')  # 숫자+문자가 아닌것 [^a-zA-Z0-9]
print(pattern.findall(text2))

pattern = re.compile('[a-z]+')  # 소문자만
print(pattern.findall(text2))

pattern = re.compile('[A-Z]+')  # 대문자만
print(pattern.findall(text2))

pattern = re.compile('[0-9]+')  # 숫자만
print(pattern.findall(text2))



pattern = re.compile('a.c')  #a와 c사이에 한개의 문자
print(pattern.search('abc'))

pattern = re.compile('a[.]c')  #a와 c사이에 . 문자
print(pattern.search('a.c'))

pattern = re.compile('ca*t')  #ct사이에 a가 0번이상 반복(없어된다)
print(pattern.search('ct'))

pattern = re.compile('ca+t')  #ct사이에 a가 1번이상 반복
print(pattern.search('caat'))

pattern = re.compile('ca{1,3}t')  #ct사이에 a가 1~3번 반복
print(pattern.search('caaat'))

pattern = re.compile('ab?c')  #a와 c사이에 b가 있거나 없거나
print(pattern.search('abc'))
