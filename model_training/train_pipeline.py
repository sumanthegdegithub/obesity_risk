import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

from model_training.config.core import config
from model_training.pipeline import obesity_risk_pipeline
from model_training.processing.data_manager import load_dataset, save_pipeline, save_label_encoder


def run_training() -> None:
    
    """
    Train the model.
    """

    # read training data
    data = load_dataset(file_name = config.training_data_file)
    
    label_encoder = LabelEncoder()
    data[config.target] = label_encoder.fit_transform(data[config.target])
    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        
        data[config.features],     # predictors
        data[config.target],       # target
        test_size = config.test_size,
        random_state=config.random_state,   # set the random seed here for reproducibility
    )
    
    # Pipeline fitting
    obesity_risk_pipeline.fit(X_train, y_train)
    #y_pred = bikeshare_pipe.predict(X_test)

    # Calculate the score/error
    #print("R2 score:", r2_score(y_test, y_pred).round(2))
    #print("Mean squared error:", mean_squared_error(y_test, y_pred))

    # persist trained model
    save_pipeline(pipeline_to_persist = obesity_risk_pipeline)
    save_label_encoder(encoder=label_encoder)
    
if __name__ == "__main__":
    run_training()