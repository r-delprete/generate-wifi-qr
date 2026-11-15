
import qrcode

from PIL import Image, ImageDraw
from qrcode.constants import ERROR_CORRECT_Q

from .wifi import build_wifi_payload


DARK = "#173C3B"
WHITE = "#FFFFFF"


def create_qr(
    ssid: str,
    password: str,
) -> Image.Image:

    payload = build_wifi_payload(ssid, password)

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_Q,
        box_size=16,
        border=4,
    )

    qr.add_data(payload)
    qr.make(fit=True)

    matrix = qr.get_matrix()

    module_size = 16
    image_size = len(matrix) * module_size

    image = Image.new("RGB", (image_size, image_size), WHITE)
    draw = ImageDraw.Draw(image)

    for y, row in enumerate(matrix):
        for x, dark in enumerate(row):
            if dark:
                x0 = x * module_size
                y0 = y * module_size

                draw.rectangle(
                    (
                        x0,
                        y0,
                        x0 + module_size - 1,
                        y0 + module_size - 1,
                    ),
                    fill=DARK,
                )

    return image
