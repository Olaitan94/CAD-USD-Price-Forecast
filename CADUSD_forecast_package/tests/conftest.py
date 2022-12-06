#This file contains code that will be used to test the config settings in config.py & config.yml

import pytest

from forecast_model.config.core import config
from forecast_model.processing.data_manager import load_dataset

#This fixture will be used to provide argument value to the prediction test
@pytest.fixture()
def desired_forecast():
    return 180
