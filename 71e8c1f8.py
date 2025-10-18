import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    def __init__(self, path='data'):
        self.path = Path(path)
        self.path.mkdir(exist_ok=True)

    def load(self, file='data.csv'):
        fp = self.path / file
        if fp.exists():
            return pd.read_csv(fp)
        return self.generate()

    def generate(self, n=100):
        np.random.seed(42)

        df = pd.DataFrame({
            'id': range(1, n + 1),
            'name': [f'Company_{i}' for i in range(1, n + 1)],
            'sector': np.random.choice(['Tech', 'Finance', 'Health'], n),
            'revenue': np.random.lognormal(12, 2, n),
            'funding': np.random.lognormal(15, 1.8, n),
            'employees': np.random.randint(5, 500, n),
            'stage': np.random.choice(['Seed', 'A', 'B', 'C'], n)
        })

        return df

    def save(self, df, file='data.csv'):
        fp = self.path / file
        df.to_csv(fp, index=False)


class DataValidator:
    def validate(self, df):
        required = ['id', 'revenue', 'funding']
        missing = [c for c in required if c not in df.columns]

        if missing:
            return {'valid': False, 'errors': missing}

        nulls = df[required].isnull().sum().sum()
        return {'valid': nulls == 0, 'nulls': nulls}


class DataCleaner:
    def clean(self, df):
        df = df.copy()
        df.columns = df.columns.str.lower()

        numeric = df.select_dtypes(include=[np.number]).columns
        for col in numeric:
            df[col] = df[col].fillna(df[col].median())

        return df
