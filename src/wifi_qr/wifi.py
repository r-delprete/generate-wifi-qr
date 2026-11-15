
def escape_wifi(value: str) -> str:
    """Escape dei caratteri riservati nel formato Wi-Fi QR."""
    for char in ("\\", ";", ",", ":", '"'):
        value = value.replace(char, "\\" + char)

    return value


def build_wifi_payload(
    ssid: str,
    password: str,
    security: str = "WPA",
    hidden: bool = False,
) -> str:
    """Costruisce il payload standard per un QR Code Wi-Fi."""

    if not ssid:
        raise ValueError("SSID non può essere vuoto.")

    if not password:
        raise ValueError("Password non può essere vuota.")

    return (
        f"WIFI:T:{security};"
        f"S:{escape_wifi(ssid)};"
        f"P:{escape_wifi(password)};"
        f"H:{str(hidden).lower()};;"
    )
