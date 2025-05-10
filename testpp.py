import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Setup ChromeDriver with options
chrome_driver_path = r"C:\\drivers\\chromedriver.exe"  # Update this to the actual path
  # Adjust this to your chromedriver path
options = Options()
options.add_argument("--headless")  # Run in headless mode (without opening the browser window)
service = Service(chrome_driver_path)

# Initialize the driver
driver = webdriver.Chrome(service=service, options=options)

# LinkedIn credentials
linkedin_username = 'vishalchakradhari6@gmail.com'
linkedin_password = 'PFPy@TjC80'

# Login function
def login():
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)

    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')

    username_input.send_keys(linkedin_username)
    password_input.send_keys(linkedin_password)

    password_input.send_keys(Keys.RETURN)
    time.sleep(3)

# Navigate to My Network and Invitations
def navigate_to_network():
    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
    time.sleep(5)

# Remove requests older than 2 months
def remove_old_requests():
    # Get the current date and calculate the threshold date
    two_months_ago = datetime.now() - timedelta(days=60)
    
    # Scroll to load all the invitations
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(10):  # Scroll 10 times
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    # Get all the invitation elements
    invitations = driver.find_elements(By.XPATH, "//div[contains(@class, 'invitation-card')]")
    
    # Loop through each invitation and check the sent date
    for invitation in invitations:
        try:
            # Get the sent date (LinkedIn shows the date, but we need to parse it)
            sent_date_element = invitation.find_element(By.XPATH, ".//span[contains(text(), 'Sent')]")
            sent_date_text = sent_date_element.text.strip()

            # Parse the sent date and check if it's older than 2 months
            sent_date = datetime.strptime(sent_date_text, "Sent %b %d, %Y")
            
            # If the sent date is older than 2 months, click "Withdraw" to remove the request
            if sent_date < two_months_ago:
                withdraw_button = invitation.find_element(By.XPATH, ".//button[text()='Withdraw']")
                withdraw_button.click()
                print(f"Withdrew request sent on: {sent_date_text}")
                time.sleep(1)  # Sleep to avoid hitting LinkedIn's rate limit
        except Exception as e:
            print(f"Error processing invitation: {e}")
            continue

# Run the process
login()
navigate_to_network()
remove_old_requests()

# Close the browser after the task is complete
driver.quit()
