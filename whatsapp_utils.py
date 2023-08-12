from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import CHROME_PROFILE_PATH

def setup_driver():
    # Set up Chrome driver with the specified profile path
    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)

    # Implicit wait to handle page loading delays
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    return driver

def wait_for_qr_scan(driver):
    # Wait for QR code to be scanned only once
    qr_scanned = False
    while not qr_scanned:
        user_input = input("Scan the QR code and press Enter when ready (or type 'done' if already scanned): ").strip().lower()
        if user_input == 'done':
            qr_scanned = True

def send_message(driver,mobile_no,message):
    try:
        search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p')
        search_box.send_keys(mobile_no)
        search_box.send_keys(Keys.RETURN)  # Send RETURN key instead of sleep


        chat_box_xpath = '/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div/div/div[8]/div/div'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, chat_box_xpath))).click()

        message_box_xpath = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, message_box_xpath))).send_keys(message,Keys.ENTER)

        print(f'"{message}" sent to {mobile_no}')

        # Wait for a few seconds after sending the message
        time.sleep(3)  # You can adjust the number of seconds as needed
    except Exception as e:
         print("An error occurred while sending the message:", str(e))

def get_user_input():
    mobile_no = input("Enter mobile number: ")
    message = input("Enter message: ")
    return mobile_no, message


