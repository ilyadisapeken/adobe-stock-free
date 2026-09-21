from pathlib import Path
import json
import re

READY_DIR = Path("ready")
OUTPUT_FILE = Path("metadata.json")


def clean_text(text):
    text = re.sub(r"[_-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def make_metadata(filename):
    name = clean_text(Path(filename).stem)

    title = name or "Professional stock image"

    keywords = [
        "business",
        "small business",
        "entrepreneur",
        "business owner",
        "online business",
        "ecommerce",
        "digital business",
        "startup",
        "marketing",
        "commerce",
        "technology",
        "professional",
        "work",
        "success"
    ]

    return {
        "filename": filename,
        "title": title,
        "description": f"Professional stock image depicting {title.lower()}.",
        "keywords": keywords,
        "ai_generated": True
    }


def main():
    results = []

    if READY_DIR.exists():
        for image in sorted(READY_DIR.iterdir()):
            if image.suffix.lower() in [".jpg", ".jpeg"]:
                results.append(make_metadata(image.name))

    OUTPUT_FILE.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Metadata dibuat untuk {len(results)} gambar.")


if __name__ == "__main__":
    main()
