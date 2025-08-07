# 🔐 StegoVault  
*A modular Python project for encrypting, hiding, detecting, and analyzing hidden data in media.*

---

## 📦 Features

- ✅ Load and preprocess images
- 🔐 AES-based encryption & decryption of secret messages
- 🖼️ **Image Steganography** with:
  - 🧱 LSB (Least Significant Bit)
- 🔍 Steganalysis support:
  - 📊 Chi-Square Test
  - 🆚 Original vs Stego Comparison
  - 🔄 RS Analysis
- 📈 CLI/Script-ready architecture for flexible usage
- ⚙️ Designed for scaling to audio, video, and text steganography

---

## 📁 Project Structure

```
StegoVault/
│
├── steganography/
│   ├── base.py                # Abstract base class for all steganography methods
│   ├── lsb_image.py           # LSB method implementation
│
├── steganalysis/
│   ├── chi_square.py          # Chi-Square statistical test
│   ├── rs_analysis.py         # RS Steganalysis
│   └── image_diff.py          # Pixel-wise image comparison
│
├── utils/
│   └── image_loader.py        # Safe loading, saving, and conversion of images
│
├── main.py                    # CLI/Entry point
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.11+
- `numpy`
- `scipy`
- `Pillow`
- `cryptography`

### 📥 Installation

```bash
git clone https://github.com/HeelinMistry/steganography.git
cd steganography
pip install -r requirements.txt
```

---


## 🛡️ Disclaimer

This tool is for **educational and ethical research** purposes only. Misuse of steganographic technology is discouraged and may violate local laws.

---

## 🤝 Contributing

Pull requests are welcome! Open an issue if you'd like to:
- Add new media types (audio, video)
- Improve robustness
- Add advanced steganalysis

---

## 📜 License

MIT License — [View License](LICENSE)