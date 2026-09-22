import os
from pathlib import Path

from gradio_client import Client

SPACE = "black-forest-labs/FLUX.1-schnell"

PROMPT = """
Professional commercial stock photograph of an Indonesian small business owner
working at a clean modern desk with a laptop, smartphone, product packaging and
notebook, natural morning light, realistic Southeast Asian appearance,
authentic modern workspace, professional business atmosphere,
subtle depth of field, high detail, sharp focus, natural skin texture,
no logos, no brands, no text, no watermark
""".strip()

OUTPUT_DIR = Path("generated")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

token = os.environ.get("HF_TOKEN")

if not token:
    raise RuntimeError("HF_TOKEN belum tersedia.")

print("Menghubungkan ke Hugging Face...")

client = Client(
    SPACE,
    token=token
)

print("Mengirim prompt ke FLUX...")

result = client.predict(
    prompt=PROMPT,
    seed=0,
    randomize_seed=True,
    width=2048,
    height=2048,
    num_inference_steps=4,
    api_name="/infer",
)

image_path = result[0]

source = Path(image_path)
output = OUTPUT_DIR / "flux_test.jpg"

source.replace(output)

print(f"Gambar berhasil dibuat: {output}")
