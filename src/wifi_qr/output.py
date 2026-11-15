from pathlib import Path

from .config import CARD
from PIL import Image


def save_png(image: Image.Image, path: Path) -> None:
    image.save(path, format="PNG", dpi=(CARD.dpi, CARD.dpi))


def save_pdf(image: Image.Image, path: Path) -> None:
    image.save(path, format="PDF", resolution=CARD.dpi)
