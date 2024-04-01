# Sentence-Spelling
## ✒ 맞춤법 검사하기

개발 기간: 5시간

개발 언어: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">

## 🔋 미리 보기
- [프로젝트 소개](#-프로젝트-소개)
- [실행 전 주의 사항](#-실행-전-주의-사항)
- [실행 영상](#-실행-영상)
- [주요 코드 설명](#-주요-코드-설명)
- [프로젝트를 하며 느낀점](#-프로젝트를-하며-느낀점)

## 🎤 프로젝트 소개
- 네이버 맞춤법 검사기는 한번에 검사가능한 300자 글자 제한이 있습니다.
- 글자가 300자가 넘어도 자동으로 맞춤법 검사해주는 프로그램입니다.
- 순서는 아래와 같습니다.
1. 메모장에 글을 적습니다.
2. 코드와 같은 디렉토리에 메모 파일을 저장합니다.
3. 네이버 맞춤법 검사하기를 통해 맞춤법 검사를 진행합니다.
4. 맞춤법 검사 완료된 파일을 따로 저장합니다.


## 🏹 실행 전 주의 사항
- https://chromedriver.chromium.org/downloads 에서 크롬 버전에 맞는 Chrome driver를 설치해야 합니다.
- 크롬 버전 확인하는 법: 크롬실행-> 브라우저 오른쪽 상단의 점 세개 클릭-> 도움말-> Chrome 정보
- 다운로드한 Chrome driver 압축을 풀고 Sentence Spelling.py와 같은 디렉토리에 위치시켜야 합니다.
- Selenium과 openpyxl을 설치해야 합니다.
  
  prompt실행 후
  ```
  pip install selenium
  pip install pyperclip
  ```

## 💿 실행 영상
![만우절 유래 맞춤법 수정](https://github.com/SeungHuiHan/Sentence-Spelling/assets/98226400/77d88e14-c57a-4d4f-b7d7-b7998f3c3298)

- 나무위키에서 만우절> 유래를 가져왔습니다.

  
## 🔊 주요 코드 설명
```python
memo_name = input("맞춤법 검사할 메모를 말해주세요: ")
file_path = f'./{memo_name}.txt'  

memo_modification_file=f'./{memo_name} _맞춤법 수정.txt'
```
- Sentence Spelling.py와 같은 디렉토리에 있는 메모중 맞춤법 검사할 메모를 입력합니다.
- 맞춤법이 수정된 메모는 원래 이름_맞춤법 수정으로 저장됩니다. (ex. 원래 메모 이름: 만우절 유래, 맞춤법 수정된 메모 이름: 만우절 유래_맞춤법 수정)


```python
with open(file_path, 'r', encoding='utf-8') as file:
    memo_content = file.read()

```
- 메모를 읽어옵니다.

```python
chunks = [memo_content[i:i+300] for i in range(0, len(memo_content), 300)]

```
- 글자를 300자씩 잘라서 리스트에 저장합니다.

```python
with open(memo_modification_file, 'a', encoding='utf-8') as file:
        file.write(memo_modification)

```
- 수정된 글을 저장합니다.
  

## 🥷 프로젝트를 하며 느낀점

구상한대로 구현한듯 하다. 

아직 아쉬운 점은 없고 계속 사용해보면서 적어나가겠다.
