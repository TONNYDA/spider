from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
import re,time,os
driver=webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url='https://www.douyu.com/g_LOL'
driver.get(url=url)

os.mkdir('斗鱼直播')
page=1
while True:
    tree = etree.HTML(driver.page_source)
    list = tree.xpath('//li[@class="layout-Cover-item"]')
    for i in list:
        title1 = i.xpath('.//h3[@class="DyListCover-intro"]/text()')[0]
        type1= i.xpath('.//span[@class="DyListCover-zone"]/text()')[0]
        zhubo1 = i.xpath('.//h2/text()')[0]
        redu1 = i.xpath('.//span/text()')[1]
        total2 = f'直播标题：{title1}\n直播类型：{type1}\n主播：{zhubo1}\n热度：{redu1}\n' + "\n"
        print(total2)
        time.sleep(0.1)

        with open(f'斗鱼直播/douyu{page}.txt','a',encoding='utf-8')as fp:
            fp.write(total2)
    driver.find_element_by_class_name('dy-Pagination-next').click()
    time.sleep(3)
    driver.save_screenshot(f'{page}.png')
    page += 1
    print(page)


