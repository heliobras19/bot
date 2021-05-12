from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def baixar(arquivo): 
    driver = webdriver.Firefox()
    driver.get("https://monitoramento.sema.mt.gov.br/simcar/tecnico.app/publico/car")
    filtro = driver.find_element_by_css_selector("div.ui:nth-child(3)")
    recibo_federal = driver.find_element_by_css_selector("div.item:nth-child(3)")
    filtro.click()
    recibo_federal.click()
    campo = driver.find_element_by_css_selector("#inputFilter")
    campo.send_keys(arquivo)
    btn = driver.find_element_by_css_selector(".primary")
    btn.click()
    try:
        down = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.primary'))
        )
        driver.execute_script("arguments[0].click();", down)
    except:
        print(arquivo)
        texto = arquivo + "\n"
        file1 = open('em-falta-brasnorte07.txt','a')
        file1.write(texto + "\n")
        file1.close()

valores = [
'MT-5101902-3E7D42D5E883426A90A8B74FC2D5B969',
'MT-5101902-42A1EFC5977D4311B21AE85318724BA8',
'MT-5101902-9941702D81254DBD96E8024AF7E0E612',
'MT-5101902-8984B72BF43D40269BCB054C6B21E2E9',
'MT-5101902-844FE69EA9ED40ED8EB5E6CCAD55176B'
]

valoresb = [

]

for a in valores:
    for b in valoresb:
        if(a == b):
            baixar(a)