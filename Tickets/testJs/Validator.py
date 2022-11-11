import json, os.path, shutil, re
from datetime import datetime


f = open('email_results.json', encoding="utf8")
data = json.load(f)

tmpFolder = "Tmp\\" #El nombre o la ruta de la carpeta debe coincidir con la ruta de la actividad Read email
rootFolder = "C:\\tmp\\"
rexgex = "[^A-Za-z0–9, ÑñÁáÉéÍíÓóÚú-]"
subjectLength = 100
date_format = "%d-%m-%Y"

for res in data:
    if(res['hasAttachment'] == True):
        for fil in res['attachments']:
            if(os.path.exists(fil['path'])):
                subject = re.sub(rexgex,"",res['subject']).strip()
                if(len(subject)>subjectLength):
                    subject = subject[0:subjectLength]
                emailDate = datetime.strptime(res['date'], '%Y-%m-%dT%H:%M:%S.%f%z')
                emailDate = emailDate.strftime(date_format)
                
                fileName = fil['path'].split(tmpFolder)
                fileName = fileName[1]
                destFolder = rootFolder+emailDate+"\\"+subject

                if not os.path.exists(destFolder):
                    os.makedirs(destFolder)

                source = fil['path']
                destination = rootFolder+emailDate+"\\"+subject+"\\"+fileName
                shutil.copy(source, destination)

    #print(rootFolder)
f.close()