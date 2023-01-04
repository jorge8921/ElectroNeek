import sys,json

data = sys.argv[1]
data = json.loads(data)


def calcular(num1, num2):
    suma = num1+num2
    resta = num1-num2
    print (str(suma)+'|'+str(resta))


for i in data:
    asig1 = i['Asig1']
    asig2 = i['Asig2']
    calcular(asig1,asig2)

#print(json.dumps(data))