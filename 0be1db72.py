import numpy as np
import pandas as pd
from dataclasses import dataclass

@dataclass
class Inputs:
    revenue: float
    growth: float
    margin: float = 0.2
    rate: float = 0.12
    years: int = 5

class Valuation:
    def __init__(self):
        self.multiples = {
            'Tech': 12.0,
            'Finance': 8.0,
            'Health': 10.0
        }

    def calculate(self, revenue, growth, margin=0.2, rate=0.12, years=5):
        fcf = self.project(revenue, growth, margin, years)
        terminal = self.terminal(fcf[-1], growth, rate)

        pv = [cf / (1 + rate) ** (i+1) for i, cf in enumerate(fcf)]
        pv_terminal = terminal / (1 + rate) ** years

        value = sum(pv) + pv_terminal

        return {
            'value': value,
            'terminal': terminal,
            'fcf': fcf
        }

    def project(self, revenue, growth, margin, years):
        fcf = []
        r = revenue

        for _ in range(years):
            r *= (1 + growth)
            ebitda = r * margin
            cf = ebitda * 0.85
            fcf.append(cf)

        return fcf

    def terminal(self, fcf, growth, rate):
        terminal_growth = min(growth * 0.5, 0.03)
        return fcf * (1 + terminal_growth) / (rate - terminal_growth)

    def comparable(self, revenue, sector):
        multiple = self.multiples.get(sector, 10.0)
        return revenue * multiple


class Risk:
    def assess(self, data):
        scores = {
            'market': self._market(data),
            'financial': self._financial(data),
            'execution': self._execution(data)
        }

        overall = sum(scores.values()) / len(scores)
        level = 'High' if overall > 0.7 else 'Medium' if overall > 0.4 else 'Low'

        return {
            'score': overall,
            'level': level,
            'breakdown': scores
        }

    def _market(self, data):
        age = data.get('age', 1)
        return 0.5 if age > 3 else 0.7

    def _financial(self, data):
        burn = data.get('burn', 1.0)
        return 0.3 if burn < 1.5 else 0.6

    def _execution(self, data):
        team = data.get('employees', 10)
        return 0.4 if team > 20 else 0.7
