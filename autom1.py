import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://servicedesk.ancora.com.br:7443/login.jsp?os_destination=%2Fprojects%2FTSD%2Fqueues%2Fcustom%2F1&permissionViolation=true')
time.sleep(2)
navegador.find_element('xpath', '//*[@id="login-form-username"]').send_keys('ezequiel.ferreira')
navegador.find_element('xpath', '//*[@id="login-form-password"]').send_keys('Mentalidad3')
navegador.find_element('xpath', '//*[@id="login-form-submit"]').click()
time.sleep(5)
navegador.find_element(By.LINK_TEXT, value='Verificar Backups').click()

time.sleep(20)