from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    timer_time = 7
    # Step 0: Set variables
    username_str = "dakotafulp@gmail.com"
    password_str = "Oz*6LTOFZ7$Ay"
    onechurch_home_page_str = "https://ekklesia.onechurchsoftware.com/"
    sms_page_str = "https://ekklesia.onechurchsoftware.com/communication/sms/schedule"


    # Step 1: Open Firefox
    browser = webdriver.Firefox(executable_path='./geckodriver')

    # Step 2: Navigate to OneChurch
    browser.get(onechurch_home_page_str)
    time.sleep(timer_time)

    # Step 3: Search and Enter Email and Password
    frame = browser.find_element_by_xpath('//*[@id="onechurch_form_login"]')
    browser.switch_to_frame(frame)
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    submit = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/form/div[4]/div[1]/eira-submit-button/button')
    username.send_keys(username_str)
    password.send_keys(password_str)
    time.sleep(timer_time)

    # Step 4: Click Login
    submit.click()
    time.sleep(timer_time)

    # Step 5: Go to Text Message Page
    browser.get(sms_page_str)
    time.sleep(timer_time)

    # Step 6: Click through all existing scheduled text messages
    current_row = 1
    current_page = 4 # Start at 3 to skip "First", "Previous Buttons", and "1" pages
    print("Working on page: 1")
    while True:
        if (current_row < 26):
            print("Working on Row: {}".format(current_row))

            # Step 6a: Click view button
            view_button_check = False
            while view_button_check != True:
                print("View Button Check")
                try:
                    view_xpath = "/html/body/div[2]/div[2]/div[4]/div[2]/div/div/div[3]/div/div/eira-tabs/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[{}]/td[7]/eira-action-menu/div/button[1]".format(current_row)
                    view_button = browser.find_element_by_xpath(view_xpath)
                    view_button.click()
                    time.sleep(timer_time)
                    view_button_check = True
                except:
                    time.sleep(timer_time)

            # Step 6b: Uncheck all previous recipients
            uncheck_button_check = False
            while uncheck_button_check != True:
                print("Uncheck Button Check")
                try:
                    uncheck_xpath = "/html/body/div[6]/div/div/div[2]/div/div/div/form/div[1]/div[1]/h4/div[1]/a[2]"
                    uncheck_button = browser.find_element_by_xpath(uncheck_xpath)
                    uncheck_button.click()
                    time.sleep(timer_time)
                    uncheck_button_check = True
                except:
                    time.sleep(timer_time)

            # Step 6c: Click add people button
            add_people_check = False
            while add_people_check != True:
                print("Add People Button Check")
                try:
                    add_people = "/html/body/div[6]/div/div/div[2]/div/div/div/form/div[1]/div[1]/h4/span/a"
                    add_people_button = browser.find_element_by_xpath(add_people)
                    add_people_button.click()
                    time.sleep(timer_time)
                    add_people_check = True
                except:
                    time.sleep(timer_time)

            # Step 6d: Click drop down button
            dropdown_check = False
            while dropdown_check != True:
                print("Dropdown Button Check")
                try:
                    dropdown = "/html/body/div[8]/div/div/div[2]/div/div[1]/div[2]/label/div/button"
                    dropdown_button = browser.find_element_by_xpath(dropdown)
                    dropdown_button.click()
                    time.sleep(timer_time)
                    dropdown_check = True
                except:
                    time.sleep(timer_time)


            # Step 6e: Click group option
            group_option_check = False
            while group_option_check != True:
                print("Group Option Button Check")
                try:
                    group_option = "/html/body/div[8]/div/div/div[2]/div/div[1]/div[2]/label/div/ul/li[2]/a"
                    group_option_button = browser.find_element_by_xpath(group_option)
                    group_option_button.click()
                    time.sleep(timer_time)
                    group_option_check = True
                except:
                    time.sleep(timer_time)

            # Step 6f: Type 365 and hit enter
            group_365_check = False
            while group_365_check != True:
                print("Group 365 Type Check")
                try:
                    group_365_str = "365"
                    group_text_box = browser.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/div[1]/div[2]/div/div/div/eira-group-autocomplete/div/div/input')
                    group_text_box.send_keys(group_365_str)
                    time.sleep(timer_time)
                    group_text_box.send_keys(Keys.RETURN)
                    time.sleep(timer_time*10)
                    group_365_check = True
                except:
                    time.sleep(timer_time)

            # Step 6g: Click Schedule SMS
            schedule_check = False
            while schedule_check != True:
                print("Schedule Button Check")
                try:
                    schedule = "/html/body/div[6]/div/div/div[2]/div/div/div/form/div[3]/div[2]/eira-submit-button/button/span[1]"
                    schedule_button = browser.find_element_by_xpath(schedule)
                    schedule_button.click()
                    time.sleep(timer_time*10)
                    schedule_check = True
                except:
                    time.sleep(timer_time)

            current_row = current_row + 1
        else:
            # Step 7: Try clicking next button
            try:
                next_option = "/html/body/div[2]/div[2]/div[4]/div[2]/div/div/div[3]/div/div/eira-tabs/div/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div[2]/ul/li[{}]/a".format(current_page)
                next_option_button = browser.find_element_by_xpath(next_option)
                page_num = int(next_option_button.get_attribute("innerHTML"))
                print("Working on page: {}".format(page_num))
                next_option_button.click()
                time.sleep(timer_time*10)
                current_row = 1
                current_page = current_page + 1
            except:
                break
    
    print("Work Completed!!!!")

if __name__ == '__main__':
    main()