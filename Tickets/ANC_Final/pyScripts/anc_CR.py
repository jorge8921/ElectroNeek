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
from getpass import getuser #agregar esta linea

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
options.add_argument('--user-data-dir=C:\\Users\\'+getuser()+'\\AppData\\Local\Google\\Chrome\\User Data') #agregar esta linea
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.delete_all_cookies() #agregar esta linea
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

#Ubicaciones CR
ubicaciones = ["rlbLocs_i154", "rlbLocs_i160", "rlbLocs_i105", "rlbLocs_i104", "rlbLocs_i103", "rlbLocs_i102", "rlbLocs_i101", "rlbLocs_i100", "rlbLocs_i99", "rlbLocs_i98", "rlbLocs_i95", "rlbLocs_i9", "rlbLocs_i94", "rlbLocs_i93", "rlbLocs_i92", "rlbLocs_i91", "rlbLocs_i90", "rlbLocs_i89", "rlbLocs_i88", "rlbLocs_i87", "rlbLocs_i86", "rlbLocs_i85", "rlbLocs_i8", "rlbLocs_i84", "rlbLocs_i83", "rlbLocs_i82", "rlbLocs_i81", "rlbLocs_i80", "rlbLocs_i79", "rlbLocs_i78", "rlbLocs_i77", "rlbLocs_i76", "rlbLocs_i75", "rlbLocs_i74", "rlbLocs_i73", "rlbLocs_i72", "rlbLocs_i71", "rlbLocs_i70", "rlbLocs_i52", "rlbLocs_i51", "rlbLocs_i4", "rlbLocs_i3", "rlbLocs_i23", "rlbLocs_i22", "rlbLocs_i21", "rlbLocs_i20", "rlbLocs_i206", "rlbLocs_i205", "rlbLocs_i204", "rlbLocs_i203", "rlbLocs_i202", "rlbLocs_i201", "rlbLocs_i200", "rlbLocs_i19", "rlbLocs_i199", "rlbLocs_i198", "rlbLocs_i197", "rlbLocs_i196", "rlbLocs_i195", "rlbLocs_i194", "rlbLocs_i193", "rlbLocs_i192", "rlbLocs_i191", "rlbLocs_i190", "rlbLocs_i18", "rlbLocs_i189", "rlbLocs_i188", "rlbLocs_i187", "rlbLocs_i186", "rlbLocs_i185", "rlbLocs_i184", "rlbLocs_i183", "rlbLocs_i182", "rlbLocs_i181", "rlbLocs_i180", "rlbLocs_i17", "rlbLocs_i179", "rlbLocs_i178", "rlbLocs_i177", "rlbLocs_i176", "rlbLocs_i175", "rlbLocs_i174", "rlbLocs_i173", "rlbLocs_i172", "rlbLocs_i171", "rlbLocs_i170", "rlbLocs_i16", "rlbLocs_i169", "rlbLocs_i168", "rlbLocs_i167", "rlbLocs_i166", "rlbLocs_i165", "rlbLocs_i164", "rlbLocs_i163", "rlbLocs_i162", "rlbLocs_i161", "rlbLocs_i159", "rlbLocs_i15", "rlbLocs_i157", "rlbLocs_i156", "rlbLocs_i155", "rlbLocs_i153", "rlbLocs_i152", "rlbLocs_i151", "rlbLocs_i150", "rlbLocs_i149", "rlbLocs_i148", "rlbLocs_i147", "rlbLocs_i14", "rlbLocs_i146", "rlbLocs_i145", "rlbLocs_i144", "rlbLocs_i143", "rlbLocs_i142", "rlbLocs_i141", "rlbLocs_i140", "rlbLocs_i139", "rlbLocs_i138", "rlbLocs_i137", "rlbLocs_i136", "rlbLocs_i135", "rlbLocs_i134", "rlbLocs_i130", "rlbLocs_i129", "rlbLocs_i128", "rlbLocs_i108", "rlbLocs_i107", "rlbLocs_i106", "rlbLocs_i10"]

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

