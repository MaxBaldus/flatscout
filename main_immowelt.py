import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np

# open chrome
driver = webdriver.Chrome() 
driver.implicitly_wait(5)

# open website login
driver.get('https://signin.immowelt.de/?target=meinbereich&path=%2Fredirect')

# enter login and handle cookies (nested shadow DOM elements)
time.sleep(30) 
# still MANUALLY -> FIX 


# log-in
mail = "maxbaldus@gmx.net"
pw = "sojxen-qAftuf-caqfo6"

login_field = driver.find_element(By.ID, 'user-name-input')
login_field.send_keys(mail)
pw_field = driver.find_element(By.ID, 'password-input')
pw_field.send_keys(pw)
anmelden = driver.find_element(By.ID, 'signin-button').click()

# go to saved searches
# FIX -> Gespeicherte Suchen
# search = driver.find_element(By.CLASS_NAME, 'udb_primaryLabel').click()
time.sleep(20)
# open saved search
# FIX -> Suche ausführen 
# search = driver.find_element(By.CLASS_NAME, 'link link--primary')
time.sleep(20)


#time.sleep(10)
#driver.maximize_window()

# open first offer
try:
    offer = driver.find_element(By.CLASS_NAME, "EstateItem-4409d").click()
    time.sleep(15)
except:
    offer = driver.find_element(By.XPATH, '//*[@id="2brb95e"]').click()
    time.sleep(15)


# contact button of first flat offer
driver.switch_to.window(driver.window_handles[1]) # switch to new tab
current_url = driver.current_url # save url

contact = driver.find_element(By.XPATH, '//*[@id="btnContactBroker"]/button')
contact.click()
time.sleep(10)
contact_final = driver.find_element(By.XPATH, '//*[@id="btnSubmitCR"]/button/span') 
contact_final.click()

# close tab again 
time.sleep(10)
driver.close()

# main loop running infinitely checking and applying for new flats every waiting_time seconds
waiting_time = np.random.uniform(20,30) # draw random number for waiting time
a = 1

while 0 < a:
    
    # switch to main tab
    driver.switch_to.window(driver.window_handles[0]) 
    time.sleep(waiting_time)

    driver.refresh() # refresh page
    time.sleep(10)
    try:
        offer = driver.find_element(By.CLASS_NAME, "EstateItem-4409d").click()
        time.sleep(10)
    except:
        offer = driver.find_element(By.XPATH, '//*[@id="2brb95e"]').click()
        time.sleep(10)
    
    # switch to new tab
    driver.switch_to.window(driver.window_handles[1]) 
    new_url = driver.current_url
    
    # compare urls and apply if new url (new offer)
    if new_url == current_url:
        time.sleep(5)
        driver.close()# close curent page (already applied to flat)       
        
    else:
        time.sleep(10)
        # send contacts
        contact = driver.find_element(By.XPATH, '//*[@id="btnContactBroker"]/button').click() 
        
        time.sleep(10)
        contact_final = driver.find_element(By.XPATH, '//*[@id="btnSubmitCR"]/button/span').click()
        current_url = driver.current_url # save new url of current flat
        
        # close tab
        time.sleep(10)
        driver.close() 

print("blub")

