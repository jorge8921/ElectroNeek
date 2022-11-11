import os, configparser, time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from datetime import datetime
from dateutil.relativedelta import relativedelta

app_path = os.path.dirname(os.path.realpath(__file__))+'/'

config_file = configparser.RawConfigParser()
config_file.read(app_path+"config.ini")
userinfo = config_file["USERINFO"]
parameters = config_file["PARAMETERS"]

# current dateTime
now = datetime.now()
# convert to string
date_time_str = now.strftime("%d/%m/%Y")
date_time_str = now + relativedelta(months=+5) # 5 meses
#Fecha hasta
fechaHasta = date_time_str.strftime("%d/%m/%Y")


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.tsdrms.net/")
driver.find_element(By.ID, "txtTsdNum").send_keys(userinfo["Account"])
driver.find_element(By.ID, "txtUsername").send_keys(userinfo["User"])
driver.find_element(By.ID, "txtPassword").send_keys(str(userinfo["Password"]))
driver.find_element(By.ID, "LoginBtn").click()
time.sleep(int(parameters["Tiempo_de_espera_web"]))
driver.get("https://www.tsdrms.net/ForecastAvailability.aspx")
time.sleep(int(parameters["Tiempo_de_espera_web"]))
print(fechaHasta)
driver.find_element(By.ID, "txtTo").clear()
driver.find_element(By.ID, "txtTo").send_keys(str(fechaHasta))

driver.find_element(By.ID, "rdAltClasses").click()

#Ubicaciones PE
ubicaciones = ["rlbLocs_i63", "rlbLocs_i64", "rlbLocs_i69", "rlbLocs_i68", "rlbLocs_i67", "rlbLocs_i66", "rlbLocs_i65", "rlbLocs_i62", "rlbLocs_i61", "rlbLocs_i60", "rlbLocs_i59", "rlbLocs_i56", "rlbLocs_i55", "rlbLocs_i54", "rlbLocs_i53", "rlbLocs_i2", "rlbLocs_i133", "rlbLocs_i132", "rlbLocs_i131", "rlbLocs_i1", "rlbLocs_i0"]

for anc in ubicaciones:
    element = driver.find_element(By.ID, anc)
    ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(element) \
    .key_up(Keys.CONTROL) \
    .perform()
    time.sleep(int(parameters["Tiempo_de_espera_anc"]))

driver.find_element(By.ID, "cbPerNoShow").clear()
driver.find_element(By.ID, "cbPerNoShow").send_keys(str("0"))

driver.find_element(By.ID, "btnRun").click()
time.sleep(int(parameters["Tiempo_de_espera_final"]))