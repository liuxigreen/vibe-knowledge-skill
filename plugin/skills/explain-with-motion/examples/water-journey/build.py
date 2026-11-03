"""One-command local example build; pass --font PATH and optionally --preview."""
from pathlib import Path
import argparse,subprocess,sys
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--font',required=True);p.add_argument('--preview',action='store_true');a=p.parse_args()
project=Path(__file__).resolve().parent;repo=project.parents[1]
subprocess.run([sys.executable,str(repo/'scripts/check_project.py'),str(project/'project.json')],check=True)
cmd=[sys.executable,str(repo/'scripts/render.py'),str(project),'--font',a.font]
if a.preview:cmd.append('--preview')
subprocess.run(cmd,check=True)
