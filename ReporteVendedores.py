import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Leer el archivo Excel
df = pd.read_excel('Excel prueba reportes.xlsx')

# Configurar Selenium y abrir WhatsApp Web
driver_path = r'chromedriver-win64/chromedriver.exe'
chrome_options = Options()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://web.whatsapp.com')

print("Escanea el código QR de WhatsApp Web.")
WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Busca un chat o inicia uno nuevo."]'))
)

for index, row in df.iterrows():
    phone = row['Telefono']
    foto_path = os.path.join(os.getcwd(), row['Foto'])

    # Buscar el contacto
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@class="selectable-text copyable-text x15bjb6t x1n2onr6"]'))
    )
    search_box.clear()
    search_box.send_keys(phone)

    time.sleep(1.5)

    try:
        # Seleccionar el contacto
        contact = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@class="x1c4vz4f x3nfvp2 xuce83p x1bft6iq x1i7k8ik xq9mrsl x6s0dn4"]'))
        )
        contact.click()
    except:
        print(f"El contacto con teléfono {phone} no fue encontrado o no se pudo seleccionar.")
        continue

    # Enviar la foto
    attach_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Adjuntar"]'))
    )
    attach_button.click()

    photo_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
    )
    photo_input.send_keys(foto_path)

    time.sleep(2)

    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Enviar"]'))
    )
    send_button.click()

    time.sleep(4)


driver.quit()