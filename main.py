import pyqrcode

link = input("Insert the link you want to be in QRCode: \n")

url = pyqrcode.create(link)
url.png("qrcode.png", scale=6)
