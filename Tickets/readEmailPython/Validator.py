import json, os.path, shutil, re
from datetime import datetime
import trace
import traceback

app_path = os.path.dirname(os.path.realpath(__file__))+'/'

f = open(app_path+'email_results.json', encoding="utf8")
data = json.load(f)

tmpFolder = "Tmp\\" #Esta es la carpeta temporal donde se guardan los adjuntos, debe coincidir con la actividad Read email
rootFolder = "C:\\tmp\\" #Esta es la carpeta raiz de destino
rexgex = "[^A-Za-z0–9, ÑñÁáÉéÍíÓóÚú-]"
subjectLength = 100 #Maximo permitido para el asunto del mail
date_format = "%d-%m-%Y" #Formato de la fecha del mail

for res in data:
    if(res['hasAttachment'] == True): #Solo emails que contengan adjuntos
        for fil in res['attachments']:
            if(os.path.exists(fil['path'])):
                subject = re.sub(rexgex,"",res['subject']).strip()
                if(len(subject)>subjectLength):
                    subject = subject[0:subjectLength].strip()
                emailDate = datetime.strptime(res['date'], '%Y-%m-%dT%H:%M:%S.%f%z')
                emailDate = emailDate.strftime(date_format)
                    
                fileName = fil['path'].split(tmpFolder)
                fileName = fileName[1]
                destFolder = rootFolder+emailDate+"\\"+subject

                if not os.path.exists(destFolder):
                        os.makedirs(destFolder)

                source = fil['path']
                destination = rootFolder+emailDate+"\\"+subject+"\\"+fileName
                if(os.path.exists(fil['path'])):
                    shutil.move(source, destination)
f.close()
