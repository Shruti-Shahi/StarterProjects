import qrcode

def generate_qrcode(text, img_name):
  qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4)
  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(img_name+".png")

url = input("Enter url to generate QR Code: ")
img_name = input("Enter name of image without the .png: ")
generate_qrcode(url, img_name)