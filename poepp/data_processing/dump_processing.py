from glob import glob
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go


def get_currency_file_paths(file_dirs="data/**/*.csv"):
    """Get all currency files. Downloaded and unzipped data dumps from poe.ninja.
    :param string: file_dirs:
        The directory to search for files in. Defaults to the data dump directory.
        Defaults to csv files. If another file type is required it should be
        specified with *.filetype.

    :returns list:
        The directory and file name of each file containing the word "currency".
    """
    csv_files = [csv_file for csv_file in glob(file_dirs, recursive=True)]
    return [currency_file for currency_file in csv_files if "currency" in currency_file]


def extract_df(file_path):
    """Extracts a dataframe from a csv file path.

    :param string: file_path
        The path of a csv file.

    :returns pd.DataFrame:
        The processed and extracted dataframe for the given poe csv data.
    """
    df = pd.read_csv(
        file_path,
        sep=";",
        parse_dates=["Date"],
        dtype={
            "League": str,
            "Get": str,
            "Pay": str,
            "Value": float,
            "Confidence": str,
        },
    )
    df.columns = df.columns.str.lower()
    df = df.rename(columns={"get": "currency"})
    df = df[df["pay"] == "Chaos Orb"]
    df = df[["league", "date", "currency", "value"]]
    return df
