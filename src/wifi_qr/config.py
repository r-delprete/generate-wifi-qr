from dataclasses import dataclass


@dataclass(frozen=True)
class CardConfig:
    width: int = 2480
    height: int = 3508
    dpi: int = 300

    reference_width: int = 1240
    reference_height: int = 1754

    background: str = "#F2F0E9"
    white: str = "#FFFFFF"
    dark: str = "#173C3B"
    muted: str = "#68716D"
    border: str = "#E5E5E0"


CARD = CardConfig()
