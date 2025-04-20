from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# ======= SET YOUR CHROMEDRIVER PATH HERE =======
chromedriver_path = "C:/Portfolio/chromedriver-win64/chromedriver.exe"  # <-- Make sure this points to the .exe file
# ===============================================

# Set up local file paths
base_path = os.path.abspath('C:/Portfolio')
pages = {
    'index': f'{base_path}/index.html',
    'deniya': f'{base_path}/deniya.html',
    'jerrica': f'{base_path}/jerrica.html',
    'shaja': f'{base_path}/shaja.html',
    'femy': f'{base_path}/femy.html',
}

# Set up Chrome WebDriver using Service
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Test index.html
    driver.get(pages['index'])
    print("Testing index.html")
    links = driver.find_elements(By.CSS_SELECTOR, ".name-box a")
    assert len(links) == 4, "All team member links not found"
    for link in links:
        print(f"Found team member link: {link.text}")

    # Test each team member page
    for name in ['deniya', 'jerrica', 'shaja', 'femy']:
        driver.get(pages[name])
        print(f"\nTesting {name}.html")
        
        # Check page title
        title = driver.title
        assert name.capitalize() in title, f"{name.capitalize()}'s title not found"
        print(f"Title check passed: {title}")

        # Check profile image
        img = driver.find_element(By.CLASS_NAME, 'profile-img')
        assert img.get_attribute('src'), "Profile image not loaded"
        print("Profile image loaded")

        # Check heading
        heading = driver.find_element(By.TAG_NAME, 'h1').text
        assert name.capitalize() in heading, f"{name.capitalize()} not in heading"
        print(f"Heading check passed: {heading}")

        # Check table
        table = driver.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        assert len(rows) >= 4, "Incomplete portfolio table"
        print(f"Table has {len(rows)} rows")

finally:
    time.sleep(2)
    driver.quit()
