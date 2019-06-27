from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\thiag\\Desktop\\Selenium\\chromedriver.exe")

driver.get("https://www.haxball.com/")
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/a").click()
driver.switch_to.frame(driver.find_element_by_tag_name("iframe")) #selecione a frame!
login_form = driver.find_element_by_xpath("/html/body/div/div/div/div/input").send_keys("mmtmn_bot")
driver.find_element_by_xpath("/html/body/div/div/div/button").click()

time.sleep(2)

frame.switch_to.driver(driver.get("https://www.haxball.com/play?c=1x5mEkdXi04"))

#driver.get("https://www.haxball.com/play?c=WfEUn16I3Jk")

