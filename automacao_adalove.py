from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import time

# Obtendo o dia atual
hoje = datetime.datetime.now().weekday()
hora = datetime.datetime.now().hour

# Credenciais no Adalove
email = 'email_adalove'
senha = 'senha_adalove'

# Verificando se é sábado (5) ou domingo (6)
if hoje in (5, 6):
    dia_semana = "sábado" if hoje == 5 else "domingo"
    print(f"Final de semana: {dia_semana}. Descanse, meu jovem!")
    exit()

# Função para configurar o driver do Chrome
def configurar_driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)

    return driver


# Configurando o driver do Chrome
driver = configurar_driver()

# Abrindo o site
driver.get("https://adalove.inteli.edu.br/home")
error = False

# Função para inserir texto em um campo com base no id
def input_by_id(id, text, class_name):
    try:
        input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, id))
        )
        input.send_keys(text)
    except:
        input_by_class_name(class_name, text)

# Função para inserir texto em um campo com base no id
def input_by_class_name(class_name, text):
    input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, class_name))
    )
    input.send_keys(text)

# Função para clicar em um elemento com base no nome da classe
def click_by_class_name(class_name):
    to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, class_name))
    )
    to_click.click()

# Função para clicar em um elemento com base no seletor css
def click_by_css_selector(css_selector):
    to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
    )
    to_click.click()


try: 
    # Inserindo o email no campo com base no id
    input_by_id(":r6:", email, "MuiInputBase-input.MuiOutlinedInput-input.css-1x5jdmq")

    # Inserindo a senha no campo com base no id
    input_by_id(":r7:", senha, "MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputAdornedEnd.css-1uvydh2")

    # Clicando no botão para logar.
    click_by_class_name("MuiButton-containedPrimary")

    time.sleep(7)

    # Clicando no icone para acessar o 'check in'
    click_by_css_selector("ul.sc-heNFcO.cXKcYk > ul > li:first-child > button")

    # Clicando no botão 'check in'
    click_by_class_name("css-1ywkuo0")

    if error:
        raise Exception("Erro ao realizar o check in")

    print("Check in realizado com sucesso")
    time.sleep(10)

except Exception as e:
    print("Erro ao realizar o check in")
    time.sleep(10)
