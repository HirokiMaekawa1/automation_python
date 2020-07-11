from selenium import webdriver
from secrets import email, password, url_for_search, url_for_accept, url_for_like, searchword1, searchword2
from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


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



#リクエストを承認
driver.get(url_for_accept)
sleep(5)

bar_btn = driver.find_element_by_class_name('msg-overlay-bubble-header')
bar_btn.click()

accepted_count = 0

while True:
    sleep(randint(2,5))
    try:
        accept_btn = driver.find_element_by_xpath('//*[text()=\"承認\"]')
        accept_btn.click()
        sleep(randint(2,5))

        accepted_count = accepted_count + 1

    except:
        break

print("Accepted %d people." % accepted_count)



#リクエストを送る1
driver.get(url_for_search)
sleep(randint(2,5))

#検索
search_box = driver.find_element_by_xpath('//*[@id="ember46"]/input')
search_box.click()
sleep(randint(2,5))

search_box.send_keys(searchword1)
sleep(randint(2,5))

search_box.send_keys(Keys.ENTER)
sleep(randint(2,5))

#ページの高さを取得
#height = driver.execute_script("return document.body.scrollHeight")
#height = height / 4


#ループ処理する
requested_count = 0


#つながり申請する
while requested_count<20:
    try:
        driver.implicitly_wait(20)
        #request_btn = driver.find_element_by_partial_link_text('つながりを申請')
        #request_btn = driver.find_elements_by_link_text("つながりを申請")
        #request_btn = driver.find_elements_by_xpath('//*[text()=\"つながりを申請\"]')
        request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
        sleep(randint(10,15))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
        #driver.scrollIntoView(request_btn)
        #driver.move_to_element(request_btn)
        #request_btn.location_once_scrolled_into_view
        #driver.location_once_scrolled_into_view(request_btn)
        #request_btn.location_once_scrolled_into_view
        sleep(randint(10,15))

        driver.execute_script("arguments[0].click();", request_btn)
        #request_btn.click()
        sleep(randint(10,15))

        done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
        sleep(randint(10,15))

        driver.execute_script("arguments[0].click();", done_btn)
        sleep(randint(10,15))

        requested_count = requested_count + 1
        print("Requested %d people." % requested_count)
        sleep(randint(10,15))

        if request_btn is False:
            break

    except NoSuchElementException:
        try:
            driver.execute_script('window.scrollTo(0, 500);')
            driver.implicitly_wait(20)

            request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
            sleep(randint(10,15))
            
            driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
            sleep(randint(10,15))

            driver.execute_script("arguments[0].click();", request_btn)
            sleep(randint(10,15))

            done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
            sleep(randint(10,15))

            driver.execute_script("arguments[0].click();", done_btn)
            sleep(randint(10,15))

            requested_count = requested_count + 1
            print("Requested %d people." % requested_count)
            sleep(randint(10,15))

            if request_btn is False:
                break
        
        except NoSuchElementException:
            try:
                driver.execute_script('window.scrollTo(0, 1000);')
                driver.implicitly_wait(20)

                request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
                sleep(randint(10,15))
                
                driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
                sleep(randint(10,15))

                driver.execute_script("arguments[0].click();", request_btn)
                sleep(randint(10,15))

                done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
                sleep(randint(10,15))

                driver.execute_script("arguments[0].click();", done_btn)
                sleep(randint(10,15))

                requested_count = requested_count + 1
                print("Requested %d people." % requested_count)
                sleep(randint(10,15))

                if request_btn is False:
                    break
            except NoSuchElementException:
                try:
                    driver.execute_script('window.scrollTo(0, 1500);')
                    driver.implicitly_wait(20)

                    request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
                    sleep(randint(10,15))
                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
                    sleep(randint(10,15))

                    driver.execute_script("arguments[0].click();", request_btn)
                    sleep(randint(10,15))

                    done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
                    sleep(randint(10,15))

                    driver.execute_script("arguments[0].click();", done_btn)
                    sleep(randint(10,15))

                    requested_count = requested_count + 1
                    print("Requested %d people." % requested_count)
                    sleep(randint(10,15))

                    if request_btn is False:
                        break

                except NoSuchElementException:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(randint(10,15))

                    next_btn = driver.find_element_by_class_name('artdeco-pagination__button--next')
                    sleep(randint(10,15))

                    driver.execute_script("arguments[0].scrollIntoView();", next_btn)
                    sleep(randint(10,15))

                    #next_btn.LocationOnScreenOnceScrolledIntoView

                    #driver.execute_script("arguments[0].location_once_scrolled_into_view();", next_btn)
                    #next_btn.location_once_scrolled_into_view
                    #sleep(randint(10,15))

                    driver.execute_script("arguments[0].click();", next_btn)
                    #next_btn.click()
                    sleep(randint(10,15))

                else:
                    print("Sending requests is done")


#リクエストを送る2
driver.get(url_for_search)
sleep(randint(2,5))

#検索
search_box = driver.find_element_by_xpath('//*[@id="ember46"]/input')
search_box.click()
sleep(randint(2,5))

search_box.send_keys(searchword2)
sleep(randint(2,5))

search_box.send_keys(Keys.ENTER)
sleep(randint(2,5))

#ページの高さを取得
#height = driver.execute_script("return document.body.scrollHeight")
#height = height / 4


#ループ処理する
requested_count = 0


#つながり申請する
while requested_count<20:
    try:
        driver.implicitly_wait(20)
        #request_btn = driver.find_element_by_partial_link_text('つながりを申請')
        #request_btn = driver.find_elements_by_link_text("つながりを申請")
        #request_btn = driver.find_elements_by_xpath('//*[text()=\"つながりを申請\"]')
        request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
        sleep(randint(10,15))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
        #driver.scrollIntoView(request_btn)
        #driver.move_to_element(request_btn)
        #request_btn.location_once_scrolled_into_view
        #driver.location_once_scrolled_into_view(request_btn)
        #request_btn.location_once_scrolled_into_view
        sleep(randint(10,15))

        driver.execute_script("arguments[0].click();", request_btn)
        #request_btn.click()
        sleep(randint(10,15))

        done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
        sleep(randint(10,15))

        driver.execute_script("arguments[0].click();", done_btn)
        sleep(randint(10,15))

        requested_count = requested_count + 1
        print("Requested %d people." % requested_count)
        sleep(randint(10,15))

        if request_btn is False:
            break

    except NoSuchElementException:
        try:
            driver.execute_script('window.scrollTo(0, 500);')
            driver.implicitly_wait(20)

            request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
            sleep(randint(10,15))
            
            driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
            sleep(randint(10,15))

            driver.execute_script("arguments[0].click();", request_btn)
            sleep(randint(10,15))

            done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
            sleep(randint(10,15))

            driver.execute_script("arguments[0].click();", done_btn)
            sleep(randint(10,15))

            requested_count = requested_count + 1
            print("Requested %d people." % requested_count)
            sleep(randint(10,15))

            if request_btn is False:
                break
        
        except NoSuchElementException:
            try:
                driver.execute_script('window.scrollTo(0, 1000);')
                driver.implicitly_wait(20)

                request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
                sleep(randint(10,15))
                
                driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
                sleep(randint(10,15))

                driver.execute_script("arguments[0].click();", request_btn)
                sleep(randint(10,15))

                done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
                sleep(randint(10,15))

                driver.execute_script("arguments[0].click();", done_btn)
                sleep(randint(10,15))

                requested_count = requested_count + 1
                print("Requested %d people." % requested_count)
                sleep(randint(10,15))

                if request_btn is False:
                    break
            except NoSuchElementException:
                try:
                    driver.execute_script('window.scrollTo(0, 1500);')
                    driver.implicitly_wait(20)

                    request_btn = driver.find_element_by_xpath('//*[text()=\"つながりを申請\"]')
                    sleep(randint(10,15))
                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", request_btn)
                    sleep(randint(10,15))

                    driver.execute_script("arguments[0].click();", request_btn)
                    sleep(randint(10,15))

                    done_btn = driver.find_element_by_xpath('//*[text()=\"完了\"]')
                    sleep(randint(10,15))

                    driver.execute_script("arguments[0].click();", done_btn)
                    sleep(randint(10,15))

                    requested_count = requested_count + 1
                    print("Requested %d people." % requested_count)
                    sleep(randint(10,15))

                    if request_btn is False:
                        break

                except NoSuchElementException:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(randint(10,15))

                    next_btn = driver.find_element_by_class_name('artdeco-pagination__button--next')
                    sleep(randint(10,15))

                    driver.execute_script("arguments[0].scrollIntoView();", next_btn)
                    sleep(randint(10,15))

                    #next_btn.LocationOnScreenOnceScrolledIntoView

                    #driver.execute_script("arguments[0].location_once_scrolled_into_view();", next_btn)
                    #next_btn.location_once_scrolled_into_view
                    #sleep(randint(10,15))

                    driver.execute_script("arguments[0].click();", next_btn)
                    #next_btn.click()
                    sleep(randint(10,15))

                else:
                    print("Sending requests is done")



"""

#投稿にイイね10個押す
driver.get(url_for_like)

liked_count = 0
while liked_count<10:
    #イイね押す処理
    liked_count = liked_count + 1

"""

