import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
import io


class qrCode:

    def __init__(self, ownerOp) -> None:
        self.Owner = ownerOp

    def Generate_code(self) -> None:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=2)

        dataString = self.Owner.par.Input.eval()

        qr.add_data(dataString)

        qr_img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer()
        )

        img_byte_arr = io.BytesIO()
        qr_img.save(img_byte_arr)
        img_byte_arr = img_byte_arr.getvalue()

        self.Owner.op('script_buffer').store('img', img_byte_arr)
        return
