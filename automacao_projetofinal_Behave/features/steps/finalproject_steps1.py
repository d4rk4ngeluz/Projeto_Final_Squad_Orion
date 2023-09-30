# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
# import requests

# @given("que o usuario esteja logado no backoffice")
# def verify_access(context):
#     response = requests.get("https://projetofinal.jogajuntoinstituto.org//")
#     if response.status_code == 200:
#         print('A solicitação foi bem-sucedida.')
#     else:
#         print(f'Falha na solicitação com o código de status {response.status_code}.')

# @when("clicar em adicionar")
# def form_text(context):
#     btn = context.browser.find_element(By.XPATH, "/html/body/div/header/section[2]/div/header/button")
#     btn.submit()

# # @when('deverei conseguir cadastrar o item "Sapato"')
# # def step_when_add_item(context):
# #     # O código para adicionar o item "Sapato" vai aqui
# #     pass

# # @when("clicar em enviar novo produto")
# # def step_when_click_send(context):
# #     # O código para clicar no botão "enviar novo produto" vai aqui
# #     pass

# # @then('deverei receber a mensagem "Produto enviado com sucesso!"')
# # def step_then_verify_message(context):
# #     # O código para verificar a mensagem de sucesso vai aqui
# #     pass
