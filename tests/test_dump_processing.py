import pandas as pd
from poepp.data_processing import dump_processing


class TestDumpProcessing:
    def test_get_csv(self):
        file_path = dump_processing.get_currency_file_paths(
            file_dirs="tests/data/*.csv"
        )
        assert file_path == ["tests/data/test_league_currency.csv"]

    def test_read_csv(self):
        file_path = dump_processing.get_currency_file_paths(
            file_dirs="tests/data/*.csv"
        )
        df = dump_processing.extract_df(file_path[0])
        assert all(df.columns == ["league", "date", "currency", "value"])
        assert df.shape == (5, 4)
