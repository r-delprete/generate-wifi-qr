
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from .config import CARD
from .qr import create_qr


FONT_DIR = Path(__file__).parent / "fonts"


def scale(value: int) -> int:
    """Scala una misura rispetto alla risoluzione di riferimento."""

    factor = min(
        CARD.width / CARD.reference_width,
        CARD.height / CARD.reference_height,
    )

    return round(value * factor)


def load_font(filename: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Carica un font locale con fallback."""

    font_path = FONT_DIR / filename

    if font_path.exists():
        return ImageFont.truetype(str(font_path), size)

    return ImageFont.load_default()


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: str,
) -> None:
    """Disegna un testo centrato orizzontalmente."""

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    x = (CARD.width - text_width) // 2

    draw.text((x, y), text, font=font, fill=fill)


def fit_font(
    text: str,
    max_width: int,
    initial_size: int,
    font_name: str = "DejaVuSans.ttf",
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Ridimensiona il font per adattarlo alla larghezza disponibile."""

    size = scale(initial_size)
    minimum_size = scale(24)
    step = max(1, scale(2))

    while size >= minimum_size:
        font = load_font(font_name, size)
        bbox = font.getbbox(text)

        if bbox[2] - bbox[0] <= max_width:
            return font

        size -= step

    return load_font(font_name, minimum_size)


def create_card(ssid: str, password: str) -> Image.Image:
    """Genera una card Wi-Fi adattabile alla risoluzione configurata."""

    image = Image.new(
        "RGB",
        (CARD.width, CARD.height),
        CARD.background,
    )

    draw = ImageDraw.Draw(image)

    # -----------------------------------
    # Font
    # -----------------------------------

    font_title = load_font("DejaVuSans.ttf", scale(76))
    font_body = load_font("DejaVuSans.ttf", scale(34))
    font_small = load_font("DejaVuSans.ttf", scale(24))
    font_label = load_font("DejaVuSans.ttf", scale(25))

    # -----------------------------------
    # Main card
    # -----------------------------------

    margin = scale(55)

    draw.rounded_rectangle(
        (
            margin,
            margin,
            CARD.width - margin,
            CARD.height - margin,
        ),
        radius=scale(55),
        fill=CARD.white,
    )

    # Decorative accent
    accent_width = scale(300)
    accent_height = scale(18)

    draw.rounded_rectangle(
        (
            (CARD.width - accent_width) // 2,
            scale(125),
            (CARD.width + accent_width) // 2,
            scale(143),
        ),
        radius=scale(9),
        fill=CARD.dark,
    )

    # -----------------------------------
    # Header
    # -----------------------------------

    draw_centered_text(
        draw,
        "WI-FI PER GLI OSPITI",
        scale(220),
        font_label,
        CARD.dark,
    )

    draw_centered_text(
        draw,
        "Benvenuto!",
        scale(310),
        font_title,
        CARD.dark,
    )

    draw_centered_text(
        draw,
        "Connettiti alla nostra rete Wi-Fi",
        scale(420),
        font_body,
        CARD.muted,
    )

    # -----------------------------------
    # QR Code
    # -----------------------------------

    qr_image = create_qr(ssid, password)

    qr_size = scale(700)
    qr_x = (CARD.width - qr_size) // 2
    qr_y = scale(535)

    qr_image = qr_image.resize(
        (qr_size, qr_size),
        Image.Resampling.NEAREST,
    )

    frame_padding = scale(20)

    draw.rounded_rectangle(
        (
            qr_x - frame_padding,
            qr_y - frame_padding,
            qr_x + qr_size + frame_padding,
            qr_y + qr_size + frame_padding,
        ),
        radius=scale(30),
        fill=CARD.white,
        outline=CARD.border,
        width=scale(3),
    )

    image.paste(qr_image, (qr_x, qr_y))

    # -----------------------------------
    # Network name
    # -----------------------------------

    ssid_font = fit_font(
        ssid,
        max_width=CARD.width - scale(300),
        initial_size=54,
    )

    draw_centered_text(
        draw,
        ssid,
        scale(1300),
        ssid_font,
        CARD.dark,
    )

    # -----------------------------------
    # Instructions
    # -----------------------------------

    draw_centered_text(
        draw,
        "Apri la fotocamera e inquadra il QR Code",
        scale(1405),
        font_small,
        CARD.muted,
    )

    draw_centered_text(
        draw,
        "per collegarti automaticamente.",
        scale(1450),
        font_small,
        CARD.muted,
    )

    # -----------------------------------
    # Footer
    # -----------------------------------

    draw.line(
        (
            scale(220),
            scale(1550),
            CARD.width - scale(220),
            scale(1550),
        ),
        fill=CARD.border,
        width=scale(2),
    )

    draw_centered_text(
        draw,
        "GRAZIE PER ESSERE QUI",
        scale(1590),
        font_label,
        CARD.muted,
    )

    return image
