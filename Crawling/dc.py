from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Chrome WebDriver 경로 설정
webdriver_service = Service('/Users/idaeho/Documents/GitHub/LLM_Toys/Crawling/chromedriver')  # Chromedriver 경로 설정
driver = webdriver.Chrome(service=webdriver_service)

# DC Inside 베스트 게시물 페이지 URL
base_url = 'https://www.dcinside.com/'

# 페이지 열기
driver.get(base_url)

# 페이지 로딩을 위해 잠시 대기
time.sleep(3)

# 베스트 게시물 목록 페이지로 이동
best_page_url = 'https://gall.dcinside.com/board/lists/?id=dcbest'
driver.get(best_page_url)

# 페이지 로딩을 위해 잠시 대기
time.sleep(3)

# 페이지 소스 가져오기
page_source = driver.page_source

# BeautifulSoup으로 페이지 파싱
soup = BeautifulSoup(page_source, 'html.parser')

# 베스트 게시물의 링크들을 추출
links = soup.select('td.gall_tit a')

# 각 게시물의 내용을 크롤링
for link in links:
    post_url = link.get('href')
    if post_url and 'board/view/' in post_url:
        # 게시물 페이지 열기
        full_url = f'https://gall.dcinside.com{post_url}'
        driver.get(full_url)
        
        # 페이지 로딩을 위해 잠시 대기
        time.sleep(3)
        
        # 게시물 페이지 소스 가져오기
        post_page_source = driver.page_source
        
        # BeautifulSoup으로 게시물 페이지 파싱
        post_soup = BeautifulSoup(post_page_source, 'html.parser')
        
        # 게시물 제목 가져오기
        title = post_soup.find('span', class_='title_subject').get_text(strip=True)
        
        # 게시물 내용 가져오기
        content = post_soup.find('div', class_='write_div').get_text(strip=True)
        
        print("Title:", title)
        print("Content:", content)
        print("="*80)

# WebDriver 종료
driver.quit()
