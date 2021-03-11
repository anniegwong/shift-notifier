import time
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from selenium import webdriver
import config

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('log-level=3')
driver = webdriver.Chrome("/Users/annie/Desktop/bin/chromedriver", chrome_options=options) # insert local path to chromedriver

driver.get('https://www.hotschedules.com/hs/login.jsp')
username = driver.find_element_by_id('loginusername')
password = driver.find_element_by_id('loginpassword')
login = driver.find_element_by_id('loginBtn')

username.send_keys(config.HSusername)
password.send_keys(config.HSpassword)
login.click()

time.sleep(6)
page = BeautifulSoup(driver.page_source, features = 'lxml')
new_tag = page.find('span', class_ = 'hs-count-badge--label')
elem = page.find('div', class_ = 'emp-home-widget-title')
file_ptr = open('C:\\Users\\annie\\Desktop\\shift_notif\\record.txt', 'r+')
if (new_tag != None):
    new_count = int(new_tag.text)
    prev_count = int(file_ptr.read())
    if (new_count > prev_count):
        file_ptr.truncate(0)
        file_ptr.seek(0)
        file_ptr.write(str(new_count))
        message = MIMEText("There is/are " + str(new_count) + " shift(s) available! :D")
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(config.gmail_user, config.gmail_password)
            message['Subject'] = "CHECK HOTSCHEDULES :D"
            message['From'] = config.sender
            message['To'] = ", ".join(config.recipients)
            server.sendmail(config.sender, config.recipients, message.as_string())
            server.quit()
            print("email sent")
        except Exception as e:
            print(e)
    else:
        file_ptr.truncate(0)
        file_ptr.seek(0)
        file_ptr.write(str(new_count))
        print("no new shifts")
elif (elem != None):
    prev_count = int(file_ptr.read())
    if (prev_count != 0):
        file_ptr.truncate(0)
        file_ptr.seek(0)
        file_ptr.write('0')
    print("no available shifts")
else:
    print("slow internet")
file_ptr.close()
print("done")

