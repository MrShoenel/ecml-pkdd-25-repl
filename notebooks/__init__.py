from pathlib import Path
from sys import path


NOTEBOOKS_DIR = Path(__file__).parent.resolve()
ROOT_DIR = NOTEBOOKS_DIR.parent.resolve()
SRC_DIR = NOTEBOOKS_DIR.parent.joinpath('./src').resolve()
REPOS_DIR = SRC_DIR.joinpath('./repos').resolve()
SCRIPTS_DIR = SRC_DIR.joinpath('./scripts').resolve()

path.append(str(ROOT_DIR))