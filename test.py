#QR CODE generator
import pyqrcode
import png 

qr = pyqrcode.create('hello')
qr.png('NEWQr1.png' , scale= 8)