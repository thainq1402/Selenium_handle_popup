from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc
import pyautogui as pg 


class GoogleDriveAutomation:
    #Init
    def __init__(self, user, password, job):
        self.user = user
        self.password = password
        self.job = job
        self.url = 'https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ec=asw-drive-hero-goto&ifkv=ARZ0qKI2KJKEBYaAw65ZAEZKKqqJnCAWR6OID_cHGTMQ8M2a-RdZFoc5W7ul2SLUu64pZOJWZF3Wsg&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-603355680%3A1711903005828954&theme=mn&ddm=0'
        self.driver = uc.Chrome()

    # Def login
    def login(self):
        # Open web
        self.driver.get(self.url)
        time.sleep(3)
        # Send user_name to the username box
        user_box = self.driver.find_element(By.NAME,'identifier')
        user_box.send_keys(self.user)
        # Click the next button
        next_button = self.driver.find_element(By.ID,'identifierNext')
        next_button.click()
        time.sleep(10)
        # Send password to the password box
        pass_box = self.driver.find_element(By.NAME,'Passwd')
        pass_box.send_keys(self.password)
        time.sleep(3)
        next_button_1 = self.driver.find_element(By.ID,'passwordNext')
        next_button_1.click()
        time.sleep(3)
        #Click the next button 

    # Def fine the job that want to move to foder
    def search_job(self):
        # Search the 1 job from job_list
        search_job = self.driver.find_element(By.CSS_SELECTOR,'input.A8sZE[jsname="oA4zhb"]')
        search_job.send_keys(self.job)
        search_job.send_keys(Keys.ENTER)
        time.sleep(3)

    # Def process move the file to a folder 
    def move_job_to_folder(self, folder_name):
        searched_key = self.driver.find_elements(By.CLASS_NAME,'KL4NAf')
        for item in searched_key:
            text = item.text
            # Check the exactly file that has to be moved
            if text == self.job:
                item.click()
                #region : 1.assign the main window to a variable
                print('===========1============') 
                main_window_handle = None
                while not main_window_handle:
                    main_window_handle = self.driver.current_window_handle
                print('===========2============') 
                #endregion
                    
                #region : 2.Click to pop up window
                print('=======3=========')
                time.sleep(3)
                # Click button move on the bar 
                move_button = self.driver.find_element(By.XPATH, '//div[@aria-label="Move"]') 
                move_button.click()
                time.sleep(10)
                print('=======4=========')
                #endregion

                #region : 3.Assign the pop up window to a variable 
                print('=======5=========')
                popup_window = None
                while not popup_window:
                    for handle in self.driver.current_window_handle:
                        if handle != main_window_handle:
                            popup_window = handle
                            break
                print('=======6=========')
                #endregion

                #region: 4.Switching to the new pop up window
                print('=======7=========')
                self.driver.switch_to.window(popup_window)
                print('=======8=========')        
                #endregion
        
                Folders = self.driver.find_elements(By.CLASS_NAME,'SHh4ze ')
                print(f'======{len(Folders)}======')
                # Get the title attribute
                time.sleep(3)
                # for folder in Folders:
                #     if folder.text == folder_name:
                #         folder.click() # Click the folder that want to move
                #         button_move = self.driver.find_element(By.XPATH, '//button[.//span[text()="Move"]]')
                #         button_move.click()
                #         break
                break

    def close(self):
        time.sleep(10)
        self.driver.close()

if __name__ == "__main__":
    user = 'xx@gmail.com'
    password = 'xx'
    job = 'Job1' # File that want to move
    folder  = 'Job1-10'
    automation = GoogleDriveAutomation(user, password, job)
    try:
        automation.login()
        automation.search_job()
        time.sleep(10)
        automation.move_job_to_folder('Job1-10')
        automation.close()
    except Exception as e:
        print(f"Exception: {e}")
