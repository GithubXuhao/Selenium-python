# coding=utf-8
from selenium import webdriver
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
fo = open("tmall_customer_reviews10.txt", "wb")
broswer = webdriver.Firefox()
broswer.maximize_window()
#1-3手机，4男裤子 5台式组装电脑   6零食  7 桌子  8手表  9电饭锅  10 鞋子
#url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.NS3hv2&id=521893618096&skuId=3141943944962&areaId=110100&cat_id=2&rn=e13f6c8554c5c738c303bf4260024afd&standard=1&user_id=263726286&is_b=1"
#url3 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.11.NS3hv2&id=522157359219&skuId=3129453692875&areaId=110100&cat_id=2&rn=e13f6c8554c5c738c303bf4260024afd&standard=1&user_id=2616970884&is_b=1"
#url4 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.4ZDZfT&id=520227142245&skuId=3123050586080&areaId=110100&cat_id=50025174&rn=1bdeadcbc1670fcfb1cd2ded3c2a4712&user_id=2228333954&is_b=1"
#url5 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.XK6TIe&id=16109378213&skuId=3115135601082&areaId=110100&cat_id=2&rn=d6991ed289675a3ef6707ea32fc95421&user_id=595397331&is_b=1"
#url6 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.31.7D4s5D&id=45724380204&skuId=104561220439&areaId=110100&cat_id=2&rn=455e44a64bc72e684c9d8156cdf5d7ec&user_id=880734502&is_b=1"
#url7 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.X1ulYQ&id=43342123536&skuId=3115979225500&areaId=110108&city=110100&posx=116.40584&posy=40.0552&cat_id=50030801&rn=5faf8e962dad18b65da08ee02854d9d8&user_id=2097896325&is_b=1"
#url8 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.XempLZ&id=39223776378&skuId=3137868377267&areaId=110100&cat_id=2&rn=7a212cfb58e48b839ea8860797cec351&user_id=2107914368&is_b=1"
#url9 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.J3gXEQ&id=523786754479&skuId=3116641846980&areaId=110100&cat_id=50938024&rn=7fd2f3fb124d0f37ae91ed20b3a09037&standard=1&user_id=2641868119&is_b=1"
url10 = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.7kyOai&id=520377909602&skuId=3129335340009&areaId=110100&cat_id=50020909&rn=ec34bcfbb37f77df36826acf7d1746e9&user_id=92688455&is_b=1"
broswer.get(url10)
time.sleep(30)
#点击商品评价
broswer.find_element_by_xpath(".//*[@id='J_TabBar']/li[2]/a").click()
time.sleep(3)
for k in range(1, 100):
    #获取到每一行的评价信息
    for i in range(1, 21):
        aaa = broswer.find_element_by_xpath(".//*[@id='J_Reviews']/div/div[6]/table/tbody/tr[" + str(i) +"]/td[1]/div[1]/div[1]").text
        fo.write(aaa)
        fo.write("\r\n")
    time.sleep(3)
    print("page " + str(k) + "done ")
    broswer.find_element_by_xpath(".//*[@id='J_TabBar']/li[2]/a").click()
    nextlink = broswer.find_element_by_xpath(".//*[@id='J_Reviews']/div/div[7]/div/a[last()]")
    nextlink.click()
    time.sleep(3)
fo.close()
