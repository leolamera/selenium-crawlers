from selenium import webdriver

# Configurações do navegador
capabilities = {
    "browserName": "chrome",
    "browserVersion": "87.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

# Execução do webdriver em cima do localhost 4444, que é o grid do selenoid
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

# Exemplo de atividade com o webdriver
driver.get("https://g1.globo.com")