from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pyperclip

# 300자 넘어가는 글자 맞춤법 검사하기 위한 자동 맞춤법 검사 프로그램
# 1. 메모장에 글을 적습니다.
# 2. 코드와 같은 디렉토리에 메모 파일을 저장합니다.
# 3. 네이버 맞춤법 검사하기를 통해 맞춤법 검사를 진행합니다.
# 4. 맞춤법 검사 완료된 파일을 따로 저장합니다.

memo_name = input("맞춤법 검사할 메모를 말해주세요: ")

# WebDriver 설정
browser = webdriver.Chrome("./chromedriver.exe") #chromedriver가 있는 파일 경로 입력
browser.get('https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=0&acr=1&ie=utf8&query=맞춤법검사기')
browser.maximize_window()

# 로컬 파일 시스템에서 메모 파일을 읽어옵니다.
file_path = f'./{memo_name}.txt'  # 메모 파일의 경로와 이름을 지정하세요.

# 맞춤법 수정한 메모를 새로 저장할 파일을 만듭니다.
memo_modification_file=f'./{memo_name} _맞춤법 수정.txt'

# 메모 파일을 읽어옵니다.
with open(file_path, 'r', encoding='utf-8') as file:
    memo_content = file.read()

# 문자 수를 계산합니다.
character_count = len(memo_content)
print('문자 수',character_count)

# 문자열을 1000자씩 나누어 리스트에 저장합니다.
chunks = [memo_content[i:i+300] for i in range(0, len(memo_content), 300)]
print('덩어리 개수',len(chunks))

for i, chunk in enumerate(chunks):

    search_box = browser.find_element(By.CSS_SELECTOR,'#grammar_checker > div > div > div.check_box > div.text_box._original > div > div.text_area > textarea')
    
    search_box.send_keys(chunk) # box선택
    browser.implicitly_wait(2)
    
    browser.find_element(By.CSS_SELECTOR,'#grammar_checker > div > div > div.check_box > div.text_box._original > div > div.check_info > button').send_keys(Keys.ENTER) # 검사하기를 실행합니다.
    browser.implicitly_wait(2)
    browser.find_element(By.CSS_SELECTOR, '#grammar_checker > div > div > div.check_box > div.text_box.right._result.result > div > div.check_info.right > div.btn_area > button.copy').send_keys(Keys.ENTER)  # 수정된 글을 복사합니다.

    # 클립보드에서 복사된 내용을 가져옵니다.
    
    memo_modification = pyperclip.paste()

     # 메모장 파일을 열고 입력된 내용을 파일에 씁니다.
    with open(memo_modification_file, 'a', encoding='utf-8') as file:
        file.write(memo_modification)
    browser.implicitly_wait(2)

    browser.find_element(By.CLASS_NAME,'delete_btn').send_keys(Keys.ENTER) # 다름 텍스트를 검사하기 위해 X버튼 눌러줍니다.

    
# 브라우저 종료
browser.quit()

