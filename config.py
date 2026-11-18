import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Ensure repository root is in sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Always load the uncommitted .env from the repo root
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# Common Settings
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AZURE_LOCATION = os.getenv("AZURE_LOCATION", "eastus")
DATA_DIR = ROOT_DIR / "data"

# Ensure data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)
