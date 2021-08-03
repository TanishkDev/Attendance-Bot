from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def clickClass(driver,words):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div[1]/div[6]/div/ol/li[46]/div[1]/div[3]/h2/a[1]/div[1]')))
        print('Yes')
        element.click()
        commenter(driver,words)
    except:
        print('Fail')


def commenter(driver,words):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body")))

        element2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]")))

        element3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]")))
        print
        element4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[5]")))

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[2]")))

        elem1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[2]/main")))

        elem2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[2]/main/section")))

        elem3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[2]/main/section/div")))

        elem4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[2]/main/section/div/div[2]")))

        elem5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[2]/main/section/div/div[2]/div[1]")))
        elem5.click()

        writeComment(driver,words)

    except:
        print("FAIL")


def writeComment(driver,words):
    comment = driver.find_element_by_xpath(
        "/html/body/div[2]/div[3]/div[4]/div[2]/div[3]/div/div[4]/div/div[2]/div[1]/div/div/div[2]")
    comment.send_keys(words)
    comment.send_keys(Keys.RETURN)
    print("YES")


# Options
option = Options()
option.add_experimental_option("debuggerAddress", "localhost:9297")

# Driver
driver = webdriver.Chrome(executable_path="chromedriver", options=option)
driver.get("https://classroom.google.com/u/1/h")
comment = input("Enter what you want to write in commnet: ")
clickClass(driver,comment)
