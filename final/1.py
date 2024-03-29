#1

import time 
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

year=input()
rank = int(input())

url1 = 'https://www.waternow.go.kr/web/ssdoData/?pMENUID=8&ATTR_1='
url2 = '&ATTR_5=5'
url = url1+year+url2
specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless') 
specific_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', options = specific_options)

header_info = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'}
page = requests.get(url, headers = header_info)
page = page.text
soup = BeautifulSoup(page, 'html.parser')

driver.get(url)
time.sleep(3)

top50_songs = soup.find_all('td') # a라는 태그를 찾아 title ellipsis 클래스만 따옴


top50_songs_list = list()
for each_data in top50_songs : #배열처럼 for문 사용할 수 있다!
  song_name = each_data.text # 텍스트만 남기기
  song_name = song_name.strip()  #strip() : 텍스트의 공백 모두 지우는 함수
  top50_songs_list.append(song_name) #수행 결과를 빈 리스트에 삽입
leaklist = []
for i in range(0, len(top50_songs_list)//11):
  num = top50_songs_list[4+11*i]
  num = num.replace(',', '')
  num = float(num)
  leaklist.append(num)
leaklist.sort()
print(int(leaklist[len(leaklist)-rank]))