# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
# import requests

# @given("que o usuario esteja na pagina do backoffice")
# def go_to_page(context):
#     context.browser.get("https://projetofinal.jogajuntoinstituto.org//")

# @when("preencher os dados de login")
# def form_text(context):
#     context.browser.find_element(By.ID, "mui-1").send_keys("orion@squadorion.org")
#     context.browser.find_element(By.ID, "outlined-adornment-password").send_keys("orion1234")

# @when("clicar em iniciar sessão")
# def form_text(context):
#     btn = context.browser.find_element(By.XPATH, "/html/body/div/main/form/button")
#     btn.submit()

# @then("deverei ter acesso ao backoffice do e-commerce")
# def verify_access(context):
#     response = requests.get("https://projetofinal.jogajuntoinstituto.org/products/")
#     if response.status_code == 200:
#         print('A solicitação foi bem-sucedida.')
#     else:
#         print(f'Falha na solicitação com o código de status {response.status_code}.')