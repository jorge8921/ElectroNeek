import os, configparser, time, json, ctypes
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getuser

from datetime import datetime
from dateutil.relativedelta import relativedelta

app_path = os.path.dirname(os.path.realpath(__file__))+'/'
jsonTotales = app_path+"/totales.json"

config_file = configparser.RawConfigParser()
config_file.read("C:\\tmp\config.ini")
userinfo = config_file["USERINFO"]
parameters = config_file["PARAMETERS"]

# current dateTime
now = datetime.now()
# convert to stringt
date_time_str = now.strftime("%d/%m/%Y")
date_time_str = now + relativedelta(days=-1) # 1 dia menos
#Fecha ayer
fechaAyer = date_time_str.strftime("%d/%m/%Y")

options = Options()
options.add_argument('--user-data-dir=C:\\Users\\'+getuser()+'\\AppData\\Local\Google\\Chrome\\User Data')
options.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def getTotal(ancList, ancName):
    driver.get("https://www.tsdrms.net/")
    driver.find_element(By.ID, "txtTsdNum").clear()
    driver.find_element(By.ID, "txtTsdNum").send_keys(userinfo["Account"])
    driver.find_element(By.ID, "txtUsername").send_keys(userinfo["User"])
    driver.find_element(By.ID, "txtPassword").send_keys(str(userinfo["Password"]))
    driver.find_element(By.ID, "LoginBtn").click()
    time.sleep(int(parameters["Tiempo_de_espera_web"]))
    driver.get("https://www.tsdrms.net/NoShowAnalysis.aspx")
    time.sleep(int(parameters["Tiempo_de_espera_web"]))

    for anc in ancList:
        element = driver.find_element(By.ID, anc)
        ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(element) \
        .key_up(Keys.CONTROL) \
        .perform()
        time.sleep(int(parameters["Tiempo_de_espera_anc"]))
    
    driver.find_element(By.ID, "txtFrom").clear()
    driver.find_element(By.ID, "txtFrom").send_keys(str(fechaAyer))

    driver.find_element(By.ID, "txtTo").clear()
    driver.find_element(By.ID, "txtTo").send_keys(str(fechaAyer))


    driver.find_element(By.ID, "btnRun").click()
    #La siguiente linea captura el valor total
    Total = WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dgNoShow_ctl00_Footer"]/tbody/tr/td[4]'))).get_attribute("innerText")

    with open(jsonTotales, "r") as jsonFile:
        data = json.load(jsonFile)

    data[ancName] = Total

    with open(jsonTotales, "w") as jsonFile:
        json.dump(data, jsonFile)
    
    #Borrar las cookies para iniciar la proxima iteración tambien puedes
    driver.delete_all_cookies()

#Ubicaciones Costa Rica
ubicaciones_CR = ["rlbLocs_i154", "rlbLocs_i160", "rlbLocs_i105", "rlbLocs_i104", "rlbLocs_i103", "rlbLocs_i102", "rlbLocs_i101", "rlbLocs_i100", "rlbLocs_i99", "rlbLocs_i98", "rlbLocs_i95", "rlbLocs_i9", "rlbLocs_i94", "rlbLocs_i93", "rlbLocs_i92", "rlbLocs_i91", "rlbLocs_i90", "rlbLocs_i89", "rlbLocs_i88", "rlbLocs_i87", "rlbLocs_i86", "rlbLocs_i85", "rlbLocs_i8", "rlbLocs_i84", "rlbLocs_i83", "rlbLocs_i82", "rlbLocs_i81", "rlbLocs_i80", "rlbLocs_i79", "rlbLocs_i78", "rlbLocs_i77", "rlbLocs_i76", "rlbLocs_i75", "rlbLocs_i74", "rlbLocs_i73", "rlbLocs_i72", "rlbLocs_i71", "rlbLocs_i70", "rlbLocs_i52", "rlbLocs_i51", "rlbLocs_i4", "rlbLocs_i3", "rlbLocs_i23", "rlbLocs_i22", "rlbLocs_i21", "rlbLocs_i20", "rlbLocs_i206", "rlbLocs_i205", "rlbLocs_i204", "rlbLocs_i203", "rlbLocs_i202", "rlbLocs_i201", "rlbLocs_i200", "rlbLocs_i19", "rlbLocs_i199", "rlbLocs_i198", "rlbLocs_i197", "rlbLocs_i196", "rlbLocs_i195", "rlbLocs_i194", "rlbLocs_i193", "rlbLocs_i192", "rlbLocs_i191", "rlbLocs_i190", "rlbLocs_i18", "rlbLocs_i189", "rlbLocs_i188", "rlbLocs_i187", "rlbLocs_i186", "rlbLocs_i185", "rlbLocs_i184", "rlbLocs_i183", "rlbLocs_i182", "rlbLocs_i181", "rlbLocs_i180", "rlbLocs_i17", "rlbLocs_i179", "rlbLocs_i178", "rlbLocs_i177", "rlbLocs_i176", "rlbLocs_i175", "rlbLocs_i174", "rlbLocs_i173", "rlbLocs_i172", "rlbLocs_i171", "rlbLocs_i170", "rlbLocs_i16", "rlbLocs_i169", "rlbLocs_i168", "rlbLocs_i167", "rlbLocs_i166", "rlbLocs_i165", "rlbLocs_i164", "rlbLocs_i163", "rlbLocs_i162", "rlbLocs_i161", "rlbLocs_i159", "rlbLocs_i15", "rlbLocs_i157", "rlbLocs_i156", "rlbLocs_i155", "rlbLocs_i153", "rlbLocs_i152", "rlbLocs_i151", "rlbLocs_i150", "rlbLocs_i149", "rlbLocs_i148", "rlbLocs_i147", "rlbLocs_i14", "rlbLocs_i146", "rlbLocs_i145", "rlbLocs_i144", "rlbLocs_i143", "rlbLocs_i142", "rlbLocs_i141", "rlbLocs_i140", "rlbLocs_i139", "rlbLocs_i138", "rlbLocs_i137", "rlbLocs_i136", "rlbLocs_i135", "rlbLocs_i134", "rlbLocs_i130", "rlbLocs_i129", "rlbLocs_i128", "rlbLocs_i108", "rlbLocs_i107", "rlbLocs_i106", "rlbLocs_i10"]
getTotal(ubicaciones_CR, "CR")

#Ubicaciones Nicaragua
ubicaciones_NI = ["rlbLocs_i111", "rlbLocs_i7", "rlbLocs_i6", "rlbLocs_i5", "rlbLocs_i127", "rlbLocs_i126", "rlbLocs_i125", "rlbLocs_i124", "rlbLocs_i123", "rlbLocs_i122", "rlbLocs_i121", "rlbLocs_i120", "rlbLocs_i119", "rlbLocs_i118", "rlbLocs_i117", "rlbLocs_i116", "rlbLocs_i115", "rlbLocs_i114", "rlbLocs_i113", "rlbLocs_i112", "rlbLocs_i110", "rlbLocs_i109"]
getTotal(ubicaciones_CR, "NI")

#Ubicaciones Guatemala
ubicaciones_GUA= ["rlbLocs_i36", "rlbLocs_i50", "rlbLocs_i49", "rlbLocs_i48", "rlbLocs_i47", "rlbLocs_i46", "rlbLocs_i45", "rlbLocs_i44", "rlbLocs_i43", "rlbLocs_i42", "rlbLocs_i41", "rlbLocs_i40", "rlbLocs_i39", "rlbLocs_i38", "rlbLocs_i37", "rlbLocs_i35", "rlbLocs_i34", "rlbLocs_i33", "rlbLocs_i32", "rlbLocs_i31", "rlbLocs_i30", "rlbLocs_i29", "rlbLocs_i28", "rlbLocs_i27", "rlbLocs_i26", "rlbLocs_i25", "rlbLocs_i24", "rlbLocs_i13", "rlbLocs_i12", "rlbLocs_i11"]
getTotal(ubicaciones_GUA, "GUA")

#Ubicaciones Peru
ubicaciones_PE = ["rlbLocs_i63", "rlbLocs_i64", "rlbLocs_i69", "rlbLocs_i68", "rlbLocs_i67", "rlbLocs_i66", "rlbLocs_i65", "rlbLocs_i62", "rlbLocs_i61", "rlbLocs_i60", "rlbLocs_i59", "rlbLocs_i56", "rlbLocs_i55", "rlbLocs_i54", "rlbLocs_i53", "rlbLocs_i2", "rlbLocs_i133", "rlbLocs_i132", "rlbLocs_i131", "rlbLocs_i1", "rlbLocs_i0"]
getTotal(ubicaciones_CR, "PE")

ctypes.windll.user32.MessageBoxW(0, "Todos los totales han sido actualizados", "Completado con exito", 1)

time.sleep(int(parameters["Tiempo_de_espera_final"]))