from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Startup Analytics API")

class ValuationRequest(BaseModel):
    revenue: float
    growth: float
    margin: float = 0.2

class RiskRequest(BaseModel):
    age: int
    burn: float
    employees: int

@app.get("/")
def root():
    return {"status": "active", "version": "1.0.0"}

@app.post("/valuation")
def valuation(req: ValuationRequest):
    from src.models import Valuation

    v = Valuation()
    result = v.calculate(
        revenue=req.revenue,
        growth=req.growth,
        margin=req.margin
    )

    return result

@app.post("/risk")
def risk(req: RiskRequest):
    from src.models import Risk

    r = Risk()
    data = {
        'age': req.age,
        'burn': req.burn,
        'employees': req.employees
    }

    return r.assess(data)

@app.get("/metrics")
def metrics(revenue: float, customers: int, marketing: float):
    from src.analytics import Metrics

    m = Metrics()
    data = {
        'revenue': revenue,
        'customers': customers,
        'marketing': marketing
    }

    return m.calculate(data)
