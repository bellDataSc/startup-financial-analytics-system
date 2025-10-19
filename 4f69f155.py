import numpy as np
import pandas as pd

class Metrics:
    def calculate(self, data):
        return {
            'cac': self.cac(data),
            'ltv': self.ltv(data),
            'runway': self.runway(data),
            'burn': self.burn(data)
        }

    def cac(self, data):
        spend = data.get('marketing', 0)
        customers = data.get('customers', 1)
        return spend / customers if customers > 0 else 0

    def ltv(self, data):
        arpu = data.get('arpu', 0)
        margin = data.get('margin', 0.5)
        churn = data.get('churn', 0.1)
        return (arpu * margin) / churn if churn > 0 else 0

    def runway(self, data):
        cash = data.get('cash', 0)
        burn = self.burn(data)
        return cash / burn if burn > 0 else float('inf')

    def burn(self, data):
        expenses = data.get('expenses', 0)
        revenue = data.get('revenue', 0)
        return max(0, expenses - revenue)


class Ratios:
    def calculate(self, data):
        return {
            'margin': self.margin(data),
            'efficiency': self.efficiency(data),
            'productivity': self.productivity(data)
        }

    def margin(self, data):
        revenue = data.get('revenue', 0)
        cost = data.get('cost', 0)
        return (revenue - cost) / revenue if revenue > 0 else 0

    def efficiency(self, data):
        revenue = data.get('revenue', 0)
        funding = data.get('funding', 1)
        return revenue / funding if funding > 0 else 0

    def productivity(self, data):
        revenue = data.get('revenue', 0)
        employees = data.get('employees', 1)
        return revenue / employees if employees > 0 else 0


class Trends:
    def analyze(self, series):
        if len(series) < 2:
            return {'growth': 0, 'trend': 'flat'}

        values = np.array(series)
        growth = (values[-1] - values[0]) / values[0]

        slope = np.polyfit(range(len(values)), values, 1)[0]
        direction = 'up' if slope > 0 else 'down' if slope < 0 else 'flat'

        return {
            'growth': growth,
            'trend': direction,
            'slope': slope
        }

    def forecast(self, series, periods=3):
        values = np.array(series)
        x = np.arange(len(values))

        slope, intercept = np.polyfit(x, values, 1)

        future_x = np.arange(len(values), len(values) + periods)
        forecast = slope * future_x + intercept

        return forecast.tolist()
