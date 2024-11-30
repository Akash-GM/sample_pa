from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Initialize the Selenium WebDriver with the path to ChromeDriver in the same directory
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")


# Wait for the search results to load
driver.implicitly_wait(3)  # Adjust the wait time as needed

# Find the search box element by name
search_box = driver.find_element(By.NAME, "q")

# Enter a search query
search_query = "Bit bucket"
search_box.send_keys(search_query)

# Submit the search
search_box.send_keys(Keys.RETURN)


# Extract and print the titles of the search results
search_results = driver.find_elements(By.XPATH, '//h3')
for result in search_results:
    print(result.text)

# Close the browser
print("closing the driver ...")
driver.quit()
