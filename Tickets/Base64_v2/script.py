import base64

file = open('C:/tmp/test.txt','rb')
encoded_data = file.read()
file.close()
decoded_data = base64.b64decode(encoded_data + b'==')

img_file = open('C:/tmp/new_image.jpeg','wb')
img_file.write(decoded_data)
img_file.close()

#encode base64
with open ("C:/tmp/descarga.png", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    print(str(my_string))

#pip install pybase64 
# pybase64 is required