# generate-wifi-qr

<p align="center">
  <strong>Generate beautiful, printable Wi-Fi QR Code cards for your guests.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-173C3B" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-not%20specified-lightgrey" alt="License not specified">
</p>

---

## Overview

**generate-wifi-qr** is a lightweight Python utility that generates Wi-Fi QR Codes and converts them into beautifully designed, printable guest cards.

Instead of manually sharing network credentials, simply print the generated card and let your guests connect by scanning the QR Code with their smartphone camera.

### Features

- **Wi-Fi QR Code generation** – Generates QR Codes using the standard Wi-Fi connection format.
- **Printable guest cards** – Creates a clean, minimalist card with a guest-friendly design.
- **Multiple export formats** – Automatically exports both PNG and PDF files.
- **Print-ready quality** – A4-sized output at 300 DPI.
- **Secure password input** – Wi-Fi passwords are entered without being displayed in the terminal.
- **Special character support** – Properly escapes reserved characters in SSIDs and passwords.
- **Bundled fonts** – Includes DejaVu Sans fonts for consistent rendering.
- **Adaptive typography** – Automatically adjusts long network names to fit the layout.

## Preview

The generated card includes:

- A welcome message.
- A scannable Wi-Fi QR Code.
- The network name (SSID).
- Simple connection instructions.

## Requirements

- Python 3.10 or newer.
- pip.

## Installation

Clone the repository:

```bash
git clone https://github.com/r-delprete/generate-wifi-qr.git
cd generate-wifi-qr
```

Install the project and its dependencies:

```bash
pip install .
```

## Usage

Run the application:

```bash
python -m wifi_qr
```

The interactive CLI will ask for the following information:

1. **Wi-Fi network name (SSID)** – The name of your guest network.
2. **Wi-Fi password** – Entered securely without terminal echo.
3. **Output directory** – An existing directory where the generated files will be saved.

Example:

```text
=== Wi-Fi Guests Card Generator ===

Nome rete Wi-Fi Guests: MyGuestNetwork
Password Wi-Fi Guests:
Output directory: ./output

Card generata correttamente!
Destinazione: output
```

The specified output directory must already exist.

## Generated Files

The application automatically generates two files using the network name as their filename prefix:

| File | Description |
|---|---|
| `MyGuestNetwork-QR.png` | High-resolution PNG image |
| `MyGuestNetwork-QR.pdf` | Print-ready PDF document |

### Output specifications

| Property | Value |
|---|---|
| Format | PNG and PDF |
| Dimensions | 2480 × 3508 pixels |
| Resolution | 300 DPI |
| Layout | A4 portrait |
| QR error correction | Level Q |
| Color scheme | Minimalist, dark green and neutral tones |

## Security

The Wi-Fi password is requested through Python's `getpass`, preventing it from being displayed while typing in the terminal.

**Important:** The generated QR Code contains the Wi-Fi credentials required for connection. Treat the resulting PNG and PDF files as sensitive information and share them only with people you trust.

## Technology Stack

- **Python** – Application logic and CLI.
- **qrcode** – Wi-Fi QR Code generation.
- **Pillow** – Image rendering, typography and file export.
- **DejaVu Sans** – Bundled typography.

## Project Structure

```text
generate-wifi-qr/
├── src/
│   └── wifi_qr/
│       ├── fonts/
│       │   ├── DejaVuSans.ttf
│       │   └── DejaVuSans-Bold.ttf
│       ├── utils/
│       ├── __init__.py
│       ├── __main__.py
│       ├── card.py
│       ├── cli.py
│       ├── config.py
│       ├── output.py
│       ├── qr.py
│       └── wifi.py
├── pyproject.toml
└── uv.lock
```

## License

No license has been specified yet.

---

<p align="center">
  Made with ❤️ to make Wi-Fi sharing easier.
</p>