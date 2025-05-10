from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)  # Keeps the browser open after script ends

# Automatically downloads the right ChromeDriver for your browser version
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



# Correct path (no extra "chromedriver/" folder)
driver_path = "C:/webdriver/chromedriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)




# LinkedIn login credentials
username = 'vishalchakradhari6@example.com'  # Replace with your LinkedIn email
password = 'PFPy@TjC80'           # Replace with your LinkedIn password

# Function to log into LinkedIn
def login():
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)

# Function to withdraw sent connection requests
def withdraw_connection_requests():
    driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')
    time.sleep(3)

    # Find the 'Sent' tab and click it
    sent_tab = driver.find_element(By.XPATH, '//button[@aria-label="Sent"]')
    sent_tab.click()
    time.sleep(2)

    # Find all the 'Withdraw' buttons for sent invitations
    withdraw_buttons = driver.find_elements(By.XPATH, '//button[@aria-label="Withdraw"]')

    # Iterate over each 'Withdraw' button and click to withdraw the connection request
    for button in withdraw_buttons:
        try:
            button.click()
            time.sleep(1)  # Add delay to avoid rate-limiting or suspicion
            print("Withdrawn a connection request")
        except Exception as e:
            print(f"Error withdrawing connection: {e}")

# Main execution flow
try:
    # Login to LinkedIn
    login()

    # Withdraw sent connection requests
    withdraw_connection_requests()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(3)  # Wait before closing the browser
    driver.quit()
