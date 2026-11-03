"""Render this example from any working directory."""
import subprocess,sys
from pathlib import Path
here=Path(__file__).resolve().parent
raise SystemExit(subprocess.call([sys.executable,str(here.parents[1]/'scripts'/'render.py'),str(here),*sys.argv[1:]]))
