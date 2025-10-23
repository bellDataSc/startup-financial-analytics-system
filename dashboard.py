dashboard_py = """import streamlit as st
import pandas as pd
import plotly.express as px
from src.data import DataLoader
from src.models import Valuation, Risk
from src.analytics import Metrics

st.set_page_config(page_title="Startup Analytics", layout="wide")

st.title("Startup Financial Analytics")

loader = DataLoader()
df = loader.load()

st.sidebar.header("Filters")
sectors = st.sidebar.multiselect("Sector", df['sector'].unique(), df['sector'].unique())
stages = st.sidebar.multiselect("Stage", df['stage'].unique(), df['stage'].unique())

filtered = df[(df['sector'].isin(sectors)) & (df['stage'].isin(stages))]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Companies", len(filtered))

with col2:
    avg_rev = filtered['revenue'].mean()
    st.metric("Avg Revenue", f"${avg_rev:,.0f}")

with col3:
    avg_fund = filtered['funding'].mean()
    st.metric("Avg Funding", f"${avg_fund:,.0f}")

with col4:
    avg_emp = filtered['employees'].mean()
    st.metric("Avg Team", f"{avg_emp:.0f}")

st.subheader("Data")
st.dataframe(filtered, use_container_width=True)

st.subheader("Funding vs Revenue")
fig = px.scatter(
    filtered,
    x='funding',
    y='revenue',
    color='sector',
    size='employees',
    hover_data=['name']
)
st.plotly_chart(fig, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.subheader("Valuation Calculator")

revenue = st.sidebar.number_input("Revenue", value=1000000, step=100000)
growth = st.sidebar.slider("Growth", 0.0, 1.0, 0.25)

if st.sidebar.button("Calculate"):
    v = Valuation()
    result = v.calculate(revenue, growth)
    st.sidebar.metric("Valuation", f"${result['value']:,.0f}")
"""

with open('dashboard.py', 'w') as f:
    f.write(dashboard_py)

print("Arquivo: dashboard.py")
print("Tamanho:", len(dashboard_py), "bytes")
print("\nRecursos:")
print("- Filtros interativos")
print("- Métricas principais")
print("- Gráfico scatter")
print("- Calculadora valuation")
