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

#Ubicaciones GT
ubicaciones = ["rlbLocs_i36", "rlbLocs_i50", "rlbLocs_i49", "rlbLocs_i48", "rlbLocs_i47", "rlbLocs_i46", "rlbLocs_i45", "rlbLocs_i44", "rlbLocs_i43", "rlbLocs_i42", "rlbLocs_i41", "rlbLocs_i40", "rlbLocs_i39", "rlbLocs_i38", "rlbLocs_i37", "rlbLocs_i35", "rlbLocs_i34", "rlbLocs_i33", "rlbLocs_i32", "rlbLocs_i31", "rlbLocs_i30", "rlbLocs_i29", "rlbLocs_i28", "rlbLocs_i27", "rlbLocs_i26", "rlbLocs_i25", "rlbLocs_i24", "rlbLocs_i13", "rlbLocs_i12", "rlbLocs_i11"]

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


