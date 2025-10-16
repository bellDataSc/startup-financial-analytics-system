Startup Financial Analytics System

Este repositório representa meu espaço de estudos e experimentação em novas tecnologias. 

Nele, aplico e testo técnicas avançadas em dados privados, baseando-me em metodologias de grande escala que costumo utilizar em dados públicos. 

Meu objetivo é evoluir continuamente essas práticas e, futuramente, integrar meus projetos e pesquisas em Machine Learning.  


## Funcionalidades

- Modelos de Valuation: DCF e múltiplos de mercado
- Métricas KPI: CAC, LTV, churn rate, burn rate  
- Dashboard Interativo: Interface Streamlit
- API REST: FastAPI para integração
- Machine Learning: Predição de sucesso
- Análise de Risco: Assessment financeiro

## Tecnologias

- Python 3.9+
- Streamlit (Dashboard)
- FastAPI (API REST)
- Pandas, NumPy (Processamento)
- Plotly (Visualização) 
- Scikit-learn (ML)
- PostgreSQL (Database)

## Autor

**Isabel Cruz**
- GitHub: https://github.com/bellDataSc
- LinkedIn: https://www.linkedin.com/in/belcruz
- Medium: https://medium.com/@belgon

Data Engineer & Business Intelligence specialist com expertise em integração e modelagem de dados de diversas fontes.

## Instalação

        ```bash
        git clone https://github.com/bellDataSc/startup-financial-analytics-system.git
        cd startup-financial-analytics-system
        pip install -r requirements.txt
        streamlit run dashboard/app.py
        ```

## Estrutura
---------------------------------------------------------------------------------
        ```
        startup-financial-analytics-system/
        ├── src/                    # Código fonte
        │   ├── data_processing/    # ETL e limpeza
        │   ├── models/            # Modelos de valuation
        │   ├── analytics/         # Cálculo de métricas
        │   ├── visualization/     # Gráficos e charts
        │   └── api/              # REST API
        ├── dashboard/            # Interface Streamlit
        ├── data/                 # Datasets
        ├── notebooks/           # Análise exploratória
        ├── tests/              # Testes unitários
        └── docs/               # Documentação

        ```

--------------------------------------------------------------------------------