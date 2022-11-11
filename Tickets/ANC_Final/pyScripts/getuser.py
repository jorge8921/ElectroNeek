import os, configparser, time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getuser

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
#options.add_argument("start-maximized")
options.add_argument("user-data-dir=C:\\Users\\"+getuser()+"\\AppData\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("google.com")
time.sleep(100)