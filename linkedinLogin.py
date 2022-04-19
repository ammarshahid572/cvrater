from selenium import webdriver
from bs4 import BeautifulSoup
import time
username="ammarshahid572@gmail.com"
password="Iamamonster"
# Creating a webdriver instance
driver = webdriver.Chrome(r"/ChromeDriver/chromedriver.exe")
# This instance will be used to log into LinkedIn
  
# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
  
# waiting for the page to load
time.sleep(3)
  
# entering username
username = driver.find_element_by_id("username")
  
# In case of an error, try changing the element
# tag used here.
  
# Enter Your Email Address
username.send_keys(username)  
  
# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element 
# tag used here.
  
# Enter Your Password
pword.send_keys(password)        
  
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()




profile_url = "https://www.linkedin.com/in/syed-ammar-hussain-557723135/"


start = time.time()
driver.get(profile_url)
initialScroll = 0
finalScroll = 1000
  
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
  
    # we will stop the script for 3 seconds so that 
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
  
    end = time.time()
  
    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 10:
        break


src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

#look for all sections with card class
sections= soup.find_all("section", {"class": "artdeco-card ember-view break-words pb3 mt4"})
for section in sections:
    print('-----------------------')
    heading = section.find_all('div', {"class":"pvs-header__title-container"})
    print("########")
    title=heading[-1].find_all('span', {"aria-hidden":"true"})
    title=title[-1].decode_contents()
    title=title.replace("<!-- -->","")
    print(title)
    print("########")
    #Check for list items
    lists=section.find_all('ul')
    for ul in lists:
        subLists=ul.find_all('li',{"class":"artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})
        for subList in subLists:
            spans=subList.find_all("span", {"class":"visually-hidden"})
            for span in spans:
                item=span.decode_contents().replace("<!-- -->","")
                print(item)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")

        
