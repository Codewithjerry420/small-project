import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5,
)

qr.add_data("https://www.instagram.com/rajibmondal82502?igsh=MWZsNmh5NzluaGxhbQ==")
qr.make(fit = True)
img = qr.make_image(fill_color = "blue", back_color = "white")
img.save("Rajib_instagram.png")