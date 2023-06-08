from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import subprocess

command="ex -s +'v/\S/d' -cwq update.txt"
subprocess.run(command, shell=True, check=True)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)
f = open('update.txt' , 'a')
f.write(dt_string+ "\n")
f.write("\n")

def run_script_for_number(num):
    try:
        # initialize the Selenium webdriver with the desired options
        options = webdriver.ChromeOptions()
        # set any desired options, such as headless mode
        # options.add_argument('--headless')
        driver = webdriver.Chrome('/Users/a.mishra/Downloads/chromedriver')
        driver.get("https://montreal.lufa.com/en/login")
        driver.find_element(By.ID, "LoginForm_user_email").send_keys("<your-email")
        driver.find_element(By.ID, "LoginForm_password").send_keys("your-password")
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/form/div[3]/input").click()
        time.sleep(1)



        driver.get("https://montreal.lufa.com/en/employee/admin")
        driver.find_element(By.NAME, "internal_employee_id").send_keys(num)
        driver.find_element(By.CSS_SELECTOR, "button").click()


        pesel = driver.find_element(By.CSS_SELECTOR, "#employee-grid td:nth-child(2)").text
        email = driver.find_element(By.CSS_SELECTOR, "#employee-grid td:nth-child(6)").text
        driver.get("https://montreal.lufa.com/en/employee/view/id/"+pesel)
        professional_email=driver.find_element(By.CSS_SELECTOR, ".half:nth-child(10) > .twothird").text
        f = open('update.txt' , 'a')
        f.write(email+"\n")
        f.write(professional_email+"\n")

        if email is not None:
            try:
                suspend_personal_email = f"/System/Volumes/Data/Users/a.mishra/bin/gam/gam update user {email} suspended on"
                subprocess.run(suspend_personal_email, shell=True, check=True)
            except Exception as e:
                print(f"something went wrong for {email}: {str(e)}")
        
        if professional_email is not None:
            try:
                suspend_professional_email = f"/System/Volumes/Data/Users/a.mishra/bin/gam/gam update user {professional_email} suspended on"
                subprocess.run(suspend_professional_email, shell=True, check=True)
            except Exception as e:
                    print(f"something went wrong for personal email {suspend_personal_email} : {str(e)} ")







        # def check_username_contains_numbers(email):
        #     username = email.split('@')[0]
        #     if any(char.isdigit() for char in username):
        #         return True
        #     else:
        #         return False
            
        # if check_username_contains_numbers(email):
        #     def remove_numbers_before_at(email):
        #         username, domain = email.split('@')
        #         username = ''.join([i for i in username if not i.isdigit()])
        #         new_email=print(username+'@'+domain)
        #         f = open('updat.txt' , 'a')
        #         f.write(new_email+"\n")
        #         exit()
        # else:
        #     exit()
        time.sleep(1)   


        driver.get("https://montreal.lufa.com/en/rights/assignment/user/id/"+pesel)
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

# example list of numbers to run the script for

numbers_list = [4583,4851,4933,4868,2433,4997,4935,2375,3247,4946]

#numbers_list = [4485,4930,4023,3376,3342,3336,4701,2481,4969,4796,4784,4738,5020,3341,4284,4717,4748,4855]
# loop through the list and run the script for each number
for num in numbers_list:
    run_script_for_number(num)
