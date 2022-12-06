import math

import pandas as pd

from forecast_model.forecast import get_forecast


def test_get_forecast(desired_forecast):
    # Given
    expected_first_prediction_value = 0.732185
    expected_no_predictions = 180

    # When
    result = get_forecast(forecast_period=desired_forecast)

    # Then
    predictions = result.get("forecast_prices")
    dates = result.get("forecast_dates")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], float)
    assert isinstance(dates, list)
    assert isinstance(dates[0], pd.Timestamp)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=100)
