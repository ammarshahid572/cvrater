from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome(r'/ChromeDriver/chromedriver.exe')

email = "#########"
password = "################"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/syed-ammar-hussain-557723135/", driver=driver)
data=person.scrape()
print(data)
