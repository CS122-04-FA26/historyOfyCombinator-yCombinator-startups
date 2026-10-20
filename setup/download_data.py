"""Download the Y Combinator startups directory (Kaggle) into ./data."""
import os
import shutil
from pathlib import Path

DATASET = "alibekmamyrbay/y-combinator-startups-full-directory-20052026"

ROOT = Path(__file__).resolve().parent
ENV_FILE = ROOT / ".env"
DATA_DIR = ROOT / "data"


def load_env() -> None:
    """Read KAGGLE_USERNAME / KAGGLE_KEY from .env if present."""
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def main() -> None:
    load_env()
    import kagglehub

    path = kagglehub.dataset_download(DATASET)
    print("Downloaded to cache:", path)

    DATA_DIR.mkdir(exist_ok=True)
    for f in Path(path).rglob("*"):
        if f.is_file():
            shutil.copy2(f, DATA_DIR / f.name)
    print("Copied into:", DATA_DIR)
    for f in sorted(DATA_DIR.iterdir()):
        if f.is_file() and f.name != ".gitkeep":
            print(f"  {f.name}  {f.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
