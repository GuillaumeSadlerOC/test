from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions

data = [
    {
        "name":"guillaume"
    }
]

vars = {}

def How():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=opts)
    driver.get("http://app1.localhost/fr/admin/")
    driver.set_window_size(1920,1012)
    driver.find_element(By.ID,"id_username").click()
    driver.find_element(By.ID,"id_username").send_keys("root")
    driver.find_element(By.ID,"id_password").click()
    driver.find_element(By.ID,"id_password").send_keys("password@")
    driver.find_element(By.CSS_SELECTOR,".submit-row > input").click()
    driver.find_element(By.LINK_TEXT,"Groupes").click()
    driver.find_element(By.CSS_SELECTOR,"li > .addlink").click()
    for item in data:
        driver.find_element(By.ID,"id_name").send_keys(Keys.DOWN)
        driver.find_element(By.ID,"id_name").send_keys(item["name"])
        driver.find_element(By.NAME,"_save").click()
    driver.close()

How()