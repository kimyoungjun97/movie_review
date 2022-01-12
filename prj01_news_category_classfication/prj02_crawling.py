from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

def crawl_title():
    driver.find_element_by_xpath('//*[@id="old_content"]/ul/li[{}]/a'.format(i)).click()
    time.sleep(0.2)
    try:
        title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p').text
        title = re.compile('[^가-힣|a-z|A-Z ]').sub(' ', title)
        print(title)
        titles.append(title)
    except NoSuchElementException:
        print('줄거리없음.{}'.format(i))
        pass
    driver.back()

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver',
                          options=options)
df_titles = pd.DataFrame()
#256
pages = [256, 287, 300, 300]
category = ['all', '12', '15', '19']
for l in range(0, 1):
    titles = []
    for k in range(1, pages[l]): #406
        url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?grade=1001001&page={}'.format(k)
        #url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}#&date=%2000:00:00&page={}'.format(l, k)
        driver.get(url)
        #time.sleep(0.5)
        for i in range(1, 21):
            try:
                 crawl_title()
            except StaleElementReferenceException:
                driver.get(url)
                print('StaleElementReferenceException')
                time.sleep(1)
                crawl_title()
            except:
                print('error')
        if k % 50 == 0:
            df_section_titles = pd.DataFrame(titles, columns=['title'])
            df_section_titles['category'] = category[l]
            df_section_titles.to_csv('./crawling/movie_{}_{}-{}.csv'.format(category[l], k-49, k), index=False)
            titles = []

    df_section_titles = pd.DataFrame(titles, columns=['title'])
    df_section_titles['category'] = category[l]
    df_section_titles.to_csv('./crawling/movie_{}_remain.csv'.format(category[l]), index = False)

df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)
df_titles.to_csv('./crawling/naver_movie.csv')
print(len(titles))
driver.close()

#//*[@id="old_content"]/ul/li[1]/a
#//*[@id="old_content"]/ul/li[2]/a



#//*[@id="content"]/div[1]/div[4]/div[1]/div/div/div/h4
#//*[@id="content"]/div[1]/div[4]/div[1]/div/div[1]/p
#//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p
#//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p
#//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p

#//*[@id="old_content"]/ul/li[1]

#//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p