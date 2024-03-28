from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
import os

# Specify the path to ChromeDriver
chrome_driver_path = "D:\emoji-downloader-animated-noto\chromedriver-win64\chromedriver.exe"  # Update this path
service = Service(executable_path=chrome_driver_path)

# Set up Selenium WebDriver with the updated method
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(service=service, options=options)

# Open the target URL
driver.get('https://googlefonts.github.io/noto-emoji-animation/')

# Wait for initial page load
time.sleep(2)  # Adjust if necessary

# Scroll to the bottom to ensure all SVGs are loaded
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load the page
    time.sleep(2)  # Adjust based on your internet speed

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find all SVG URLs and their corresponding names
svg_elements = driver.find_elements(By.CSS_SELECTOR, "img[src*='/s/e/notoemoji/latest/']")
save_directory = "downloaded_gifs"
os.makedirs(save_directory, exist_ok=True)

order_counter = 1  # Counter to prefix filenames with

for svg_element in svg_elements:
    svg_url = svg_element.get_attribute('src')
    # Assuming the name is in the next sibling span element
    emoji_name = svg_element.find_element(By.XPATH, "following-sibling::span").text
    
    if 'emoji.svg' in svg_url and emoji_name:
        gif_url = svg_url.replace('emoji.svg', '512.gif')
        
        # Sanitize the emoji name to create a valid filename
        safe_name = emoji_name.replace("-", "_").replace(" ", "_")
        
        if safe_name == "":
            continue  # Skip if the name is empty after sanitization
        
        # Check if the file already exists and create a unique name if necessary
        original_path = os.path.join(save_directory, f'{safe_name}.gif')
        file_path = original_path
        counter = 1
        while os.path.exists(f"{order_counter}_{file_path}"):
            file_path = os.path.join(save_directory, f'{safe_name}_{counter}.gif')
            counter += 1
        
        # Download the GIF
        response = requests.get(gif_url)
        if response.status_code == 200:
            final_path = os.path.join(save_directory, f'{order_counter}_{safe_name}.gif' if counter == 1 else f'{order_counter}_{safe_name}_{counter}.gif')
            with open(final_path, 'wb') as file:
                file.write(response.content)
            print(f'Successfully downloaded {final_path}')
            order_counter += 1  # Increment the order counter after a successful download
        else:
            print(f'Failed to download GIF for {emoji_name}')

# Clean up by closing the Selenium WebDriver
driver.quit()
