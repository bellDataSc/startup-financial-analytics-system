tests_py = """import pytest
import pandas as pd
from src.data import DataLoader, DataValidator, DataCleaner
from src.models import Valuation, Risk
from src.analytics import Metrics, Ratios, Trends

def test_data_loader():
    loader = DataLoader()
    df = loader.generate(n=10)
    
    assert len(df) == 10
    assert 'revenue' in df.columns
    assert df['revenue'].notna().all()

def test_data_validator():
    validator = DataValidator()
    df = pd.DataFrame({'id': [1], 'revenue': [1000], 'funding': [5000]})
    
    result = validator.validate(df)
    assert result['valid'] == True

def test_valuation():
    v = Valuation()
    result = v.calculate(revenue=1000000, growth=0.25)
    
    assert 'value' in result
    assert result['value'] > 0
    assert len(result['fcf']) == 5

def test_comparable_valuation():
    v = Valuation()
    value = v.comparable(revenue=1000000, sector='Tech')
    
    assert value > 0

def test_risk_assessment():
    r = Risk()
    data = {'age': 3, 'burn': 1.2, 'employees': 25}
    result = r.assess(data)
    
    assert 'score' in result
    assert 'level' in result
    assert 0 <= result['score'] <= 1

def test_metrics_calculation():
    m = Metrics()
    data = {
        'marketing': 10000,
        'customers': 100,
        'arpu': 50,
        'margin': 0.5,
        'churn': 0.1
    }
    
    result = m.calculate(data)
    
    assert 'cac' in result
    assert 'ltv' in result
    assert result['cac'] == 100
    assert result['ltv'] > 0

def test_ratios():
    r = Ratios()
    data = {'revenue': 1000, 'cost': 600, 'employees': 10}
    result = r.calculate(data)
    
    assert 'margin' in result
    assert result['margin'] == 0.4

def test_trends():
    t = Trends()
    series = [100, 120, 140, 160]
    result = t.analyze(series)
    
    assert result['trend'] == 'up'
    assert result['growth'] > 0

def test_forecast():
    t = Trends()
    series = [100, 110, 120]
    forecast = t.forecast(series, periods=2)
    
    assert len(forecast) == 2
    assert all(f > 120 for f in forecast)
"""

with open('tests.py', 'w') as f:
    f.write(tests_py)

print("Arquivo: tests.py")
print("Tamanho:", len(tests_py), "bytes")
print("\nTestes criados:")
print("- test_data_loader")
print("- test_data_validator")
print("- test_valuation")
print("- test_risk_assessment")
print("- test_metrics_calculation")
print("- test_ratios")
print("- test_trends")
print("- test_forecast")