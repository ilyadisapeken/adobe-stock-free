from PIL import Image
import sys
from pathlib import Path

MIN_MP = 4
MAX_MP = 100
MAX_FILE_MB = 45


def check_image(image_path):
    path = Path(image_path)

    if not path.exists():
        print("❌ File tidak ditemukan")
        return False

    file_mb = path.stat().st_size / (1024 * 1024)

    if file_mb > MAX_FILE_MB:
        print(f"❌ File terlalu besar: {file_mb:.2f} MB")
        return False

    try:
        image = Image.open(path)
        image.load()
    except Exception as e:
        print(f"❌ Gambar tidak bisa dibaca: {e}")
        return False

    width, height = image.size
    megapixels = (width * height) / 1_000_000

    print("=== ADOBE STOCK QC ===")
    print(f"File      : {path.name}")
    print(f"Resolusi  : {width} × {height}")
    print(f"Megapixel : {megapixels:.2f} MP")
    print(f"Format    : {image.format}")
    print(f"Mode      : {image.mode}")
    print(f"Ukuran    : {file_mb:.2f} MB")

    passed = True

    if image.format != "JPEG":
        print("❌ Format harus JPEG")
        passed = False
    else:
        print("✅ Format JPEG")

    if megapixels < MIN_MP:
        print("❌ Resolusi terlalu kecil")
        passed = False
    elif megapixels > MAX_MP:
        print("❌ Resolusi terlalu besar")
        passed = False
    else:
        print("✅ Resolusi memenuhi batas")

    if image.mode not in ("RGB", "RGBA"):
        print(f"⚠️ Mode warna: {image.mode}")
    else:
        print("✅ Mode warna RGB/RGBA")

    print()

    if passed:
        print("🟢 QC LULUS")
        return True

    print("🔴 QC GAGAL")
    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cara menggunakan:")
        print("python qc/check_image.py nama_gambar.jpg")
        sys.exit(1)

    check_image(sys.argv[1])
