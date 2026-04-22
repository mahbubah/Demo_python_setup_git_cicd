import numpy as np


def replace_sentinel(df, sentinel=-999):
    return df.replace(sentinel, np.nan)


def celsius_to_fahrenheit(temp_c):
    return (temp_c * 9 / 5) + 32
