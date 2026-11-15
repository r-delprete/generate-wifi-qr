from PIL import ImageFont
from pathlib import Path


def load_font(name: str, size: int, font_dir: str | Path):
    if isinstance(font_dir, str):
        font_dir = Path(font_dir)

    path = font_dir / name
    if path.exists():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()
