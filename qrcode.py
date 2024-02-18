import pyqrcode
from PIL import Image

qr_kod = pyqrcode.create("https://www.linkedin.com/in/naif-binici-763726251/?originalSubdomain=tr")
cikti = "qr_kod.png"
qr_kod.png(cikti,scale=10)
cerceve = Image.open(cikti)
cerceve.show() 