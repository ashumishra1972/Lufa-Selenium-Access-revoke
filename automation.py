from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

def run_script_for_number(num):
    try:
        # initialize the Selenium webdriver with the desired options
        options = webdriver.ChromeOptions()
        # set any desired options, such as headless mode
        driver = webdriver.Chrome('/Users/a.mishra/Downloads/chromedriver')
        driver.get("https://montreal.lufa.com/en/login")
        driver.find_element(By.ID, "LoginForm_user_email").send_keys("<Pass-your-email-here>")
        driver.find_element(By.ID, "LoginForm_password").send_keys("<Pass-your-Credentials-here")
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/form/div[3]/input").click()
        time.sleep(1)



        driver.get("https://montreal.lufa.com/en/employee/admin")
        driver.find_element(By.NAME, "internal_employee_id").send_keys(num)
        driver.find_element(By.CSS_SELECTOR, "button").click()


        pesel = driver.find_element(By.CSS_SELECTOR, "#employee-grid td:nth-child(2)").text
        email = driver.find_element(By.CSS_SELECTOR, "#employee-grid td:nth-child(6)").text
        driver.get("https://montreal.lufa.com/en/employee/view/id/"+pesel)
        professional_email=driver.find_element(By.CSS_SELECTOR, ".half:nth-child(10) > .twothird").text
        f = open('updateded1.txt' , 'a')
        f.write(professional_email+"\n")
        f.write(email+"\n")
        time.sleep(1)   


        driver.get("https://montreal.lufa.com/en/rights/assignment/user/id/"+pesel)
        driver.get("https://montreal.lufa.com/en/employee/view/id/"+pesel)
        try:
            for i in range(20):
                driver.find_element(By.ID, "yt0").click()
                time.sleep(1)
                driver.refresh()
                time.sleep(1)
        except NoSuchElementException:
            driver.get("https://montreal.lufa.com/en/users/admin")
            driver.find_element(By.NAME, "Users[user_id]").send_keys(pesel)
            driver.find_element(By.ID, "yw2").click()
            driver.find_element(By.LINK_TEXT, "Active").click()
            driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div/form/div/div[1]/div[1]/select/option[1]").click()
            driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div/form/div/div[1]/div[2]/button[1]").click()
        # perform any desired actions on the webpage
        
        # close the webdriver
        driver.quit()
        
    except WebDriverException as e:
        print(f'Error occurred for number {num}: {e}')
        # handle the error in any desired way, such as logging or notifying
        pass


numbers_list = [Pass-Emloyer-d-code-here]
# loop through the list and run the script for each number
for num in numbers_list:
    run_script_for_number(num)
