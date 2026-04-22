import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

import pandas as pd
from src.utils import replace_sentinel, celsius_to_fahrenheit


def test_replace_sentinel_replaces_minus999():
    df = pd.DataFrame({'T2M': [-999, 25.0, -999]})
    result = replace_sentinel(df)
    assert result['T2M'].isna().sum() == 2


def test_replace_sentinel_keeps_valid():
    df = pd.DataFrame({'T2M': [20.0, 25.0, 30.0]})
    result = replace_sentinel(df)
    assert result['T2M'].isna().sum() == 0


def test_celsius_freezing_point():
    assert celsius_to_fahrenheit(0) == 32.0


def test_celsius_boiling_point():
    assert celsius_to_fahrenheit(100) == 212.0
