import os
import qrcode
from PIL import Image

# QR kodunun içereceği URL'yi kullanıcıdan al
url = input("QR kodu içerecek URL: ")

# QR kodunu oluştur
qr = qrcode.QRCode(version=None, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

# QR kodunu Pillow kütüphanesi kullanarak PNG olarak kaydet
img = qr.make_image(fill_color="black", back_color="white")
img_path = os.path.join(os.getcwd(), "qrcode.png")
img.save(img_path)

print(f"QR kodu başarıyla oluşturuldu ve {img_path} adresinde kaydedildi.")
