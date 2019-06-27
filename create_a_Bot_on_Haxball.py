from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\thiag\\Desktop\\Selenium\\chromedriver.exe") #local do webdriver

driver.get("https://www.haxball.com/") #site do jogo
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/a").click() #primeiro botão do jogo
driver.switch_to.frame(driver.find_element_by_tag_name("iframe")) #selecione a frame!
login_form = driver.find_element_by_xpath("/html/body/div/div/div/div/input").send_keys("mmtmn_bot") #cria o nome do personagem
driver.find_element_by_xpath("/html/body/div/div/div/button").click() #seleciona botão para criar nick
