import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inicializa o navegador
driver = webdriver.Chrome()

# Acessa a página de cadastro
driver.get("http://127.0.0.1:8000/authentication/create-account/")

time.sleep(2)  # Espera para carregar a página

# Preenche os campos do formulário
driver.find_element(By.NAME, "first_name").send_keys("Luiz")
time.sleep(1)
driver.find_element(By.NAME, "last_name").send_keys("Felipe")
time.sleep(1)
driver.find_element(By.NAME, "email").send_keys("luiz@example.com")
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys("luiz123")
time.sleep(1)
driver.find_element(By.NAME, "password1").send_keys("SenhaForte123")
time.sleep(1)
driver.find_element(By.NAME, "password2").send_keys("SenhaForte123")
time.sleep(4)
driver.find_element(By.NAME, "cpf").send_keys("00956423744")
time.sleep(4)
driver.find_element(By.NAME, "telefone").send_keys("(61) 91234-5678")
time.sleep(1)
driver.find_element(By.NAME, "data_nascimento").send_keys("01012000")
time.sleep(1)

# Submete o formulário
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(10)  # Espera para verificar a resposta

# Fecha o navegador
driver.quit()

