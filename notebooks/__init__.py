from pathlib import Path
from sys import path
import shutil


NOTEBOOKS_DIR = Path(__file__).parent.resolve()
ROOT_DIR = NOTEBOOKS_DIR.parent.resolve()
SRC_DIR = NOTEBOOKS_DIR.parent.joinpath('./src').resolve()
REPOS_DIR = SRC_DIR.joinpath('./repos').resolve()
CSFLOW_DIR = REPOS_DIR.joinpath('./cs_flow').resolve()
SCRIPTS_DIR = SRC_DIR.joinpath('./scripts').resolve()

path.append(str(ROOT_DIR))



def activate_cs_flow_config(name: str) -> None:
    # First, we activate the correct configuration.
    assert CSFLOW_DIR.exists()
    default_config = CSFLOW_DIR.joinpath('./config.py')
    if default_config.exists():
        default_config.unlink()

    config = CSFLOW_DIR.joinpath(f'./config_{name}.py')
    assert config.exists()
    shutil.copy(src=config, dst=default_config)
