from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
# Iniciar o webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Quais são os passos a fazer?

# 1 - Navegar até https://automatize.netlify.app/
driver.get('https://automatize.netlify.app')
sleep(2)
# Encontrar o elemento
campo_email = driver.find_element(By.ID,'email')
sleep(2)
# 2 - Clicar no campo de e-mail
campo_email.click()
sleep(2)
# 3 - Digitar um e-mail
campo_email.send_keys('jhonatan@hotmail.com')
sleep(2)
# encontrar campo senha
campo_senha = driver.find_element(By.XPATH,"//input[@type='password']")
sleep(2)
# 4 - Clicar no campo de senha
campo_senha.click()
sleep(2)
# 5 - Digitar uma senha
campo_senha.send_keys('123456')
sleep(2)
# 6 - Clicar no botão iniciar
botao_iniciar = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
sleep(2)
botao_iniciar.click()
input()