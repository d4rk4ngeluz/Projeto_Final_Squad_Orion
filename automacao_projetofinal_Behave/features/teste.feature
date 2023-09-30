#language: pt

Funcionalidade: Login e Cadastro de Item com Sucesso

    Como colaborador do backoffice Joga Junto
    Quero efetuar login no portal e cadastrar itens

    Cenário: Login e Cadastro de Item - Sapato

    Dado que o usuario esteja na pagina do backoffice
    Quando preencher os dados de login
    E clicar em iniciar sessão
    Então deverei ter acesso ao backoffice do e-commerce
    Quando clicar em adicionar
    E conseguir cadastrar o item "Sapato"
    E clicar em enviar novo produto
    Então deverei receber a mensagem "Produto enviado com sucesso!"