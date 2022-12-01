import xml.etree.ElementTree as ET

xmlfile = 'C:\\tmp\\nestle.xml'

def readXML(xml):
    data = ""
    try:
        tree = ET.parse(xml)
        root = tree.getroot()
        for child in root:
            data = data+" | "+str(child.text)
        return data
    except Exception as err:
       error = f'Error: {err}'
       return error

print(readXML(xmlfile))