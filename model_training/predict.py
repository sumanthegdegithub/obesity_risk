import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Union
import pandas as pd
import numpy as np

from model_training import __version__ as _version
from model_training.config.core import config
from model_training.processing.data_manager import load_pipeline, load_encoder
from model_training.processing.validation import validate_inputs


pipeline_file_name = f"{config.pipeline_save_file}{_version}.pkl"
obesity_risk_pipe = load_pipeline(file_name = pipeline_file_name)

encoder_file_name = f"{config.encoder_save_file}{_version}.pkl"
encoder = load_encoder(file_name = encoder_file_name)


def make_prediction(*, input_data: Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model """
    
    validated_data, errors = validate_inputs(input_df = pd.DataFrame(input_data))
    validated_data = validated_data.reindex(columns = config.features)
    results = {"predictions": None, "version": _version, "errors": errors}
      
    if not errors:
        predictions = obesity_risk_pipe.predict(validated_data)
        predictions = encoder.inverse_transform(predictions)
        results = {"predictions": predictions, "version": _version, "errors": errors}
        
    return results



if __name__ == "__main__":

    data_in = {
        'Gender': ['Male'],
        'Age':[24.443011],
        'Height': [1.699998],
        'Weight': [81.66995],
        'family_history_with_overweight': ['yes'],
        'FAVC': ['yes'],
        'FCVC': [2],
        'NCP': [2.983297],
        'CAEC': ['Sometimes'],
        'SMOKE': ['no'],
        'CH2O': [2.763573],
        'SCC': ['no'],
        'FAF': [0],
        'TUE': [0.976473],
        'CALC': ['Sometimes'],
        'MTRANS' : ['Public_Transportation'],
    }

    print(make_prediction(input_data = data_in))