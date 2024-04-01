# Sentence-Spelling
## ✒ 맞춤법 검사하기

개발 기간: 4시간

개발 언어: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">

## 🔎 미리 보기
- [프로젝트 소개](#-프로젝트-소개)
- [실행 전 주의 사항](#-실행-전-주의-사항)
- [실행 영상](#-실행-영상)
- [주요 코드 설명](#-주요-코드-설명)
- [프로젝트를 하며 느낀점](#-프로젝트를-하며-느낀점)

## 🗿 프로젝트 소개
- 금융기사를 찾아서 공부하면서 키워드 중심으로 기사를 뽑아낼 수 있을까 생각으로 개발하였습니다.
- 순서는 아래와 같습니다.
1. 네이버 검색창에 검색하고 싶은 뉴스의 키워드로 검색합니다.
2. 뉴스를 관련도순 또는 최신순 보기를 선택할 수 있습니다.
3. 상위 10개 기사를 크롤링하여 엑셀로 정리합니다.
4. 엑셀에는 기사 제목, 언론사, 게시 시간, 기사 링크로 정리됩니다.
5. 링크를 클릭하면 해당 기사가 뜹니다.


## 💣 실행 전 주의 사항
- https://chromedriver.chromium.org/downloads 에서 크롬 버전에 맞는 Chrome driver를 설치해야 합니다.
- 크롬 버전 확인하는 법: 크롬실행-> 브라우저 오른쪽 상단의 점 세개 클릭-> 도움말-> Chrome 정보
- 다운로드한 Chrome driver 압축을 풀고 CGV IMAX Movie reservation program.py과 같은 디렉토리에 위치시켜야 합니다.
- Selenium과 Beautifulsoup4,openpyxl을 설치해야 합니다.
  
  prompt실행 후
  ```
  pip install selenium
  pip install bs4
  pip install openpyxl
  ```

## 📸 실행 영상
![푸바오 기사](https://github.com/SeungHuiHan/News-Keyword-Search/assets/98226400/6f30e3f7-a073-42b4-a9c7-bd2f272fb891)

## 🎹 주요 코드 설명
```python
Keyword = input("검색할 뉴스의 키워드를 말해주세요: ")
prefer = int(input("뉴스를 관련도순으로 볼려면 1 최신순으로 볼려면 2를 입력하세요: "))
```
- 검색할 뉴스의 키워드를 입력합니다. (ex. 푸바오)
- 뉴스를 관련도순으로 정리하려면 1를
- 최신순으로 정리하려면 2를 입력합니다.
- 뉴스는 지면기사를 기준으로 검색됩니다.


```python
# 데이터프레임 생성
df = pd.DataFrame(data, columns=['제목', '언론사', '게시 시간', '링크'])

# 엑셀 파일 저장
now = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
excel_file_name = f"{Keyword} {'관련도순' if prefer == 1 else '최신순'} 뉴스 ({now}).xlsx"
df.to_excel(excel_file_name, index=False)

```
- 기사 제목, 언론사, 게시 시간, 기사 링크순으로 엑셀에 정리됩니다.
- 엑셀이름은 키워드+관련도순 or최신순+해당 프로그램을 실행한 날짜로 이루어집니다. (ex. 푸바오 최신순 뉴스 (202404011900))


## 😹 프로젝트를 하며 느낀점

구상한대로 구현을 하였다. 

다만, 기사의 주요 단어를 뽑아내는 프로그램을 만들고 싶었는데 그건 ML 알고리즘을 사용해야 한다.

난이도가 높아 구현은 못했지만 앞으로 시도해볼 것이다! 
