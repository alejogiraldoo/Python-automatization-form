from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Instalando el controlador para Chrome (chromeDriver)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Abre el formulario
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdGimtjBQeJ_el-yroJqPr05Pwg7qvYfLoNBKSTAwXRxFJWNg/viewform")
time.sleep(8)
# ____________________________________________________
# Elementos del formulario
inputCorreo = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')                        
inputActividad = driver.find_element(By.XPATH, '//*[@id="i20"]/div[3]/div')
inputAsignatura = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
inputNombreDocente = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
inputLaboratorio = driver.find_element(By.XPATH, '//*[@id="i71"]/div[2]')
inputEquipoUtilizado = driver.find_element(By.XPATH, '//*[@id="i103"]/div[2]')
# ____________________________________________________
# Llenado del formulario (Selectores)
# ROL                                      
selectRol = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div')
selectRol.click()
time.sleep(4)
inputRol = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/span')
inputRol.click()
# ASOCIACION
time.sleep(4)
selectAsociacion = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div')
selectAsociacion.click()
time.sleep(4)
inputAsociacion = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]/span')
inputAsociacion.click()
# HORA DE INGRESO
time.sleep(4)
selectHoraIngreso = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div')
selectHoraIngreso.click()
time.sleep(4)
inputHoraIngreso = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[7]/span')
inputHoraIngreso.click()
# HORA DE FINALIZACION
time.sleep(4)
selectHoraFinalizacion = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div')
selectHoraFinalizacion.click()
time.sleep(4)
inputHoraFinalizacion = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[2]/div[15]/span')
inputHoraFinalizacion.click()

# Llenado del formulatio (Inputs)
time.sleep(4)
inputCorreo.send_keys("alejandrogiraldoocampo@pascualbravo.edu.co")
inputActividad.click()
inputAsignatura.send_keys("Simulación e impresion 3D")
inputNombreDocente.send_keys("Carlos Pino")
inputLaboratorio.click()
inputEquipoUtilizado.click()
#-----------------------------------------------------
# Enviar formulario
botonSiguiente = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
botonSiguiente.click()
time.sleep(4)
botonEnviar = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
botonEnviar.click()
# Mantiene la ventana abierta en segundos (100 segundos)
time.sleep(2)
# Cierra la ventana
driver.close()
driver.quit()