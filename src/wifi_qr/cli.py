from getpass import getpass
from pathlib import Path

from .card import create_card
from .output import save_png, save_pdf


def main() -> None:
    print("=== Wi-Fi Guests Card Generator ===\n")

    ssid = input("Nome rete Wi-Fi Guests: ").strip()
    password = getpass("Password Wi-Fi Guests: ")
    output_dir = Path(input("Output directory: ").strip())

    if not ssid or not password:
        raise ValueError("SSID e password sono obbligatori.")

    if not output_dir.exists():
        raise Exception(f"Il percorso {output_dir} non esiste.")

    image = create_card(ssid, password)
    filename = {
        'pdf': f"{ssid}-QR.pdf",
        'png': f"{ssid}-QR.png"
    }

    save_png(image, output_dir / filename["png"])
    save_pdf(image, output_dir / filename["pdf"])

    print("\nCard generata correttamente!")
    print(f"Destinazione: {output_dir}")


if __name__ == "__main__":
    main()
