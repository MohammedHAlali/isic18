from pathlib import Path
import os

import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input

import isic_data
import keras_model_utilities as kmu

_OUTPUT_PATH = Path("/home/helle246/data/isic_models/inception")

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

if __name__ == '__main__':
    # Get callbacks for training/validation
    callbacks = kmu.get_callbacks(_OUTPUT_PATH)

    # Make data pipeline
    trds = isic_data.get_iterator("trn", 32, 299, preprocess_input)
    vads = isic_data.get_iterator("val", 32, 299, preprocess_input)

    # Run training
    kmu.run_training_stage(_OUTPUT_PATH, 200,
        np.arange(start=0, stop=313).tolist(), 0.0001, callbacks, trds, vads,
        InceptionV3
    )
