from whatsapp_utils import setup_driver,wait_for_qr_scan,send_message,get_user_input
def main():
    try:
        #setup the driver
        driver = setup_driver()

        #wait for QR code scan
        wait_for_qr_scan(driver)

        # Get user input for mobile number and message
        mobile_no,message = get_user_input()

        #send the message
        send_message(driver,mobile_no,message)

        #close the driver
        driver.quit()
    except Exception as e:
        print("An error occurred ", str(e))

if __name__ == "__main__":
    main()
