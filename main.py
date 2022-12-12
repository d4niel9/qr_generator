import qrcode

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer, RoundedModuleDrawer, SquareModuleDrawer, VerticalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask, VerticalGradiantColorMask, HorizontalGradiantColorMask, SquareGradiantColorMask, SolidFillColorMask


def menu():
    instructions = """
    *******************************************
                    QR GENERATOR
    * Instructions:
    - Enter text to QR
    - Enter name image QR to generate
    *******************************************
    """
    print(instructions)

def qr():
    #Generte QR object
    text = input("Text: >>> ")
    name_file = input("Name image QR: >>> ")
    qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=9,
                    border=3,)
    
    qr.add_data(text)
    qr.make(fit=True)

    # Edit style QR
    img = qr.make_image(back_color=(255, 0, 0), fill_color=(0, 0, 0))  # Color RGB QR
    ##img = qr.make_image(fill_color="blue", back_color="yellow") # Color
    ###tipoQRC = CircleModuleDrawer() # Type QR Style
    ###colorQR = RadialGradiantColorMask() # Color QR
    ###img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC, color_mask=colorQR)
    
    # Save QR
    f = open("./output/" + name_file, "wb")
    img.save(f)
    f.close()


def main():
    menu()
    qr()


if __name__ == "__main__":
  main()
