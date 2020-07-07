from selenium import webdriver
from secrets import email, password, url_for_search, url_for_accept, url_for_like, searchword1
from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get(url_for_search)
sleep(randint(2,5))

to_login = driver.find_element_by_xpath("/html/body/div/main/p/a") 
to_login.click()
sleep(randint(2,5))

email_in = driver.find_element_by_xpath('//*[@id="username"]')
email_in.click()
email_in.send_keys(email)
sleep(randint(2,5))

password_in = driver.find_element_by_xpath('//*[@id="password"]')
password_in.click()
password_in.send_keys(password)
sleep(randint(2,5))

login_btn = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
login_btn.click()
sleep(randint(2,5))


#検索
search_box = driver.find_element_by_xpath('//*[@id="ember46"]/input')
search_box.click()
sleep(randint(2,5))

search_box.send_keys(searchword1)
sleep(randint(2,5))

search_box.send_keys(Keys.ENTER)
sleep(randint(2,5))


#ループ処理する
requested_count = 0
while True:
    try:
        request_btn = driver.find_elements_by_link_text('つながりを申請')
        request_btn.location_once_scrolled_into_view
        request_btn.click()
        sleep(randint(2,5))

        done_btn = driver.find_element_by_xpath('//*[@id="ember721"]')
        done_btn.click()
        requested_count = requested_count + 1
        sleep(randint(2,5))

    except:
        next_btn = driver.find_element_by_xpath('//*[@id="ember849"]')
        next_btn.location_once_scrolled_into_view
        next_btn.click()
        sleep(randint(2,5))
        
    print("Requested %d people." % requested_count)






"""
#申請を承認
driver.get(url_for_accept)
sleep(5)

bar_btn = driver.find_element_by_class_name('msg-overlay-bubble-header')
bar_btn.click()

accepted_count = 0

while True:
    sleep(randint(2,5))
    try:
        accept_btn = driver.find_element_by_class_name('invitation-card__action-btn')
        accept_btn.click()
        sleep(2)

        accepted_btn = driver.find_element_by_class_name('artdeco-button--muted')
        accepted_btn.click()
        accepted_count = accepted_count + 1
    except:
        break
print("Accepted %d people." % accepted_count)


#イイね10個押す
driver.get(url_for_like)

i = 0
while i<5:
    #イイね押す処理
    i = i + 1


"""

