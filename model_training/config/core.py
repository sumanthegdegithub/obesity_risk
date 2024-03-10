# Path setup, and access the config.yml file, datasets folder & trained models
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from pathlib import Path
from typing import Dict, List

from pydantic import BaseModel
from strictyaml import YAML, load

import model_training

# Project Directories
PACKAGE_ROOT = Path(model_training.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
#print(CONFIG_FILE_PATH)

DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
ENCODER_DIR = PACKAGE_ROOT / "encoder_models"


class AppConfig(BaseModel):
    """
    Application-level config.
    """

    package_name: str
    training_data_file: str
    pipeline_name: str
    pipeline_save_file: str
    encoder_save_file: str


class ModelConfig(BaseModel):
    """
    All configuration relevant to model
    training and feature engineering.
    """

    target: str
    features: List[str]
    
    Gender: str
    Age: str
    Height: str
    Weight: str
    family_history_with_overweight: str
    FAVC: str
    FCVC: str
    NCP: str
    CAEC: str
    SMOKE: str
    CH2O: str
    SCC: str
    FAF: str
    TUE: str
    CALC: str
    MTRANS : str
    
    test_size:float
    random_state: int
    n_estimators: int
    max_depth: int


class Config(BaseModel):
    """Master config object."""

    package_name: str
    training_data_file: str
    pipeline_name: str
    pipeline_save_file: str
    encoder_save_file: str
    
    target: str
    features: List[str]
    
    Gender: str
    Age: str
    Height: str
    Weight: str
    family_history_with_overweight: str
    FAVC: str
    FCVC: str
    NCP: str
    CAEC: str
    SMOKE: str
    CH2O: str
    SCC: str
    FAF: str
    TUE: str
    CALC: str
    MTRANS : str
    
    test_size:float
    random_state: int
    n_estimators: int
    max_depth: int

def find_config_file() -> Path:
    """Locate the configuration file."""
    
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    
    raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
        
    raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()
    # specify the data attribute from the strictyaml YAML type.
    _config = Config(**parsed_config.data)
        
    return _config


config = create_and_validate_config()