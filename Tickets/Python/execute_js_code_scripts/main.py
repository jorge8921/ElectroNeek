import xml.etree.ElementTree as ET, getpass as gt

try:
    file_path = r"C:\users\\"+gt.getuser()+"\Documents\Tickets\Python\execute_js_code_scripts\\" #Este es el directirio raiz de la carpeta donde estan los xml
    xml_file = open(file_path+"plants.xml") #Apertura / abrir
    #print(xml_file.read())
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_plants = xml_data.findall('PLANT')
        for plant in lst_plants:
            print('Nombre: {}'.format(plant.find('COMMON').text))
            print('Botanica: {}'.format(plant.find('BOTANICAL').text))
            print(f'Precio: {plant.find("PRICE").text}')
            print('--------------------------------------------------')
        #print(len(plant))
        #print(lst_plants)
        #print(True)
        #print(xml_data)
    else:
        print(False)
except Exception as err:
    print(f'Error: {err}')
finally:
    xml_file.close()