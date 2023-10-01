from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import requests
import pyautogui


@given("que o usuario esteja na pagina do backoffice")
def go_to_page(context):
    context.browser.get("https://projetofinal.jogajuntoinstituto.org//")

@when("preencher os dados de login")
def form_text(context):
    context.browser.find_element(By.ID, "mui-1").send_keys("orion@squadorion.org")
    context.browser.find_element(By.ID, "outlined-adornment-password").send_keys("orion1234")

@when("clicar em iniciar sessão")
def form_text(context):
    btn = context.browser.find_element(By.XPATH, "/html/body/div/main/form/button")
    btn.submit()

@then("deverei ter acesso ao backoffice do e-commerce")
def verify_access(context):
    response = requests.get("https://projetofinal.jogajuntoinstituto.org//")
    if response.status_code == 200:
        print('A solicitação foi bem-sucedida.')
    else:
        print(f'Falha na solicitação com o código de status {response.status_code}.')

pyautogui.PAUSE = 5

@given("que o usuario esteja logado no backoffice")
def verify_access(context):
    response = requests.get("https://projetofinal.jogajuntoinstituto.org/products/")
    if response.status_code == 200:
        print('A solicitação foi bem-sucedida.')
    else:
        print(f'Falha na solicitação com o código de status {response.status_code}.')


pyautogui.PAUSE = 5
# sleep(5)

@when("clicar em adicionar")
def form_text(context):
    pyautogui.click(x=1216, y=24)
    pyautogui.click(x=1791, y=736)

pyautogui.PAUSE = 5
# sleep(5)

# @when('deverei conseguir cadastrar o item "Sapato"')
# def form_text(context):
@when(u'conseguir cadastrar o item "Sapato"')
def step_impl(context):
    context.browser.find_element(By.ID, "mui-2").send_keys("Tênis Infantil Vivi Star")
    sleep(0.5)
    context.browser.find_element(By.ID, "mui-3").send_keys("Tênis Infantil Tam 34")
    sleep(0.5)
    context.browser.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[2]").click()
    sleep(0.5)
    context.browser.find_element(By.ID, "mui-4").send_keys("105,50")
    sleep(0.5)
    context.browser.find_element(By.ID, "mui-6").send_keys("20,00")
    sleep(0.5)
    pyautogui.click(x=865, y=725)
    pyautogui.write("D:\IJJ\Itensdesafio\Tenis_infantil.jpg")
    pyautogui.press("Enter")
  


@when("clicar em enviar novo produto")
def form_text(context):
    btn = context.browser.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/button")
    btn.submit()


@then('deverei receber a mensagem "Produto enviado com sucesso!"')
def verify_access(context):
    response = requests.get("https://projetofinal.jogajuntoinstituto.org/products/")
    if response.status_code == 201:
        print('Produto enviado com sucesso!')
    else:
        print(f'Falha na solicitação com o código de status {response.status_code}.')