from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from datetime import timedelta
import time


def main():
    timer_time = 3
    # Step -1: Read in text message information list
    input_file = open('365Days.csv', 'r', encoding='utf-8-sig')
    text_messages = []
    count = 34
    while True:
        # Get line of input file
        line = input_file.readline()

        # Parse line and store results
        if not line:
            break
        else:
            res = line.split(".")
            day = res[0].strip()
            date = str((datetime.now() + timedelta(days=count)).strftime("%b %-d"))
            verse = res[1].strip()
            target_date = str((datetime.now() + timedelta(days=count)).strftime("%m/%d/%Y"))
            text_messages.append([day, date, verse, target_date])
            count = count + 1
            print(text_messages[-1])

    input_file.close()

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
    time.sleep(timer_time*3)

    # Step 5: Go to Text Message Page
    browser.get(sms_page_str)
    time.sleep(timer_time)


    # Step 6: Click through all existing scheduled text messages
    current_row = 0
    while True:
        try:
            # Step 6a: Click create new text message
            new_xpath = "/html/body/div[2]/div[2]/div[4]/div[2]/div/div/div[3]/div/div/eira-tabs/div/div/div/div[3]/div/div/div/div/button"
            new_button = browser.find_element_by_xpath(new_xpath)
            new_button.click()
            time.sleep(timer_time)

            # Step 6b: Click add people button
            add_people = "/html/body/div[6]/div/div/div[2]/div/div/div/form/div[1]/div[1]/h4/span/a"
            add_people_button = browser.find_element_by_xpath(add_people)
            add_people_button.click()
            time.sleep(timer_time)

            # Step 6c: Click drop down button
            dropdown = "/html/body/div[8]/div/div/div[2]/div/div[1]/div[2]/label/div/button"
            dropdown_button = browser.find_element_by_xpath(dropdown)
            dropdown_button.click()
            time.sleep(timer_time)

            # Step 6d: Click group option
            group_option = "/html/body/div[8]/div/div/div[2]/div/div[1]/div[2]/label/div/ul/li[2]/a"
            group_option_button = browser.find_element_by_xpath(group_option)
            group_option_button.click()
            time.sleep(timer_time)

            # Step 6e: Type 365 and hit enter
            group_365_str = "365"
            group_text_box = browser.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/div[1]/div[2]/div/div/div/eira-group-autocomplete/div/div/input')
            group_text_box.send_keys(group_365_str)
            time.sleep(2)
            group_text_box.send_keys(Keys.RETURN)
            time.sleep(timer_time*10)

            # Step 6f: Type Day and Bible verse
            text = "Ekklesia 1 Year Chronological Bible Reading Plan\n{} * {}\nRead {}".format(text_messages[current_row][0], text_messages[current_row][1], text_messages[current_row][2])
            message_text_box = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div/div/form/div[1]/div[2]/eira-sms-composer/div/div[1]/textarea')
            message_text_box.send_keys(text)
            time.sleep(timer_time)

            # Step 6g: Turn off replies
            no_repiles_option = "/html/body/div[6]/div/div/div[2]/div/div/div/form/div[1]/div[3]/div/div/label[2]"
            no_repiles_option_button = browser.find_element_by_xpath(no_repiles_option)
            no_repiles_option_button.click()
            time.sleep(timer_time)

            # Step 6h: Type in target date and time
            date_box = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div/div/form/div[2]/div[2]/eira-date-time-select/div/span/input')
            date_box.clear()
            date_box.send_keys(text_messages[current_row][3])
            date_box.send_keys(Keys.RETURN)
            time.sleep(timer_time)
            time_box = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div/div/form/div[2]/div[2]/eira-date-time-select/div/div/input')
            time_box.clear()
            time_box.send_keys("7:00AM")
            time_box.send_keys(Keys.RETURN)
            time.sleep(timer_time)

            # Step 6i: Schedule Text
            schedule = "/html/body/div[6]/div/div/div[2]/div/div/div/form/div[3]/div[2]/eira-submit-button/button/span[1]"
            schedule_button = browser.find_element_by_xpath(schedule)
            schedule_button.click()
            time.sleep(timer_time*10)

            current_row = current_row + 1
        except:
            break

    print("Work Completed!!!!")

if __name__ == '__main__':
    main()