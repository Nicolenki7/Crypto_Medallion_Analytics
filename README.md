# 📊 Crypto Medallion Analytics

**Medallion Architecture for DeFi | PySpark | MLflow | Power BI Dashboard**

[![Microsoft Fabric](https://img.shields.io/badge/Microsoft_Fabric-F34F21?logo=microsoft)](https://fabric.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E3492F?logo=apachespark)](https://spark.apache.org/)
[![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow)](https://mlflow.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

Complete data pipeline implementing **Bronze → Silver → Gold** Medallion Architecture for cryptocurrency market analysis with predictive ML models. Built on Microsoft Fabric with PySpark ETL, MLflow tracking, and Power BI visualization.

This project demonstrates production-ready patterns for DeFi analytics with volume-backed trend validation and signal-vs-noise analysis.

---

## 💼 Business Impact

- **Signal-vs-Noise Analysis**: Filters market volatility to identify actionable trends
- **Volume-Backed Validation**: Correlates price movements with trading volume
- **Risk/Volume Correlation**: Understand relationship between volatility and liquidity
- **ML-Driven Insights**: Linear Regression price prediction with tracked experiments

---

## 🛠️ Technical Stack

| Category | Technologies |
| :--- | :--- |
| **Platform** | Microsoft Fabric |
| **Data Engineering** | PySpark, Dataflows Gen2 |
| **Data Storage** | OneLake, Delta Lake (Bronze/Silver/Gold) |
| **Machine Learning** | Linear Regression, MLflow |
| **BI & Analytics** | Power BI, DAX |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              CRYPTO MEDALLION ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  BRONZE LAYER (Raw)                                         │
│  └─→ Raw crypto prices from APIs                            │
│      - No transformation, immutable storage                 │
│                                                              │
│  SILVER LAYER (Cleaned)                                     │
│  └─→ Validated, deduplicated, type-corrected                │
│      - Schema enforcement, null handling                    │
│                                                              │
│  GOLD LAYER (Business-Ready)                                │
│  └─→ Aggregated features for analytics                      │
│      - Monthly metrics, volatility, volume                  │
│      - ML-ready feature sets                                │
│                                                              │
│  ML LAYER (Predictions)                                     │
│  └─→ Linear Regression with MLflow tracking                 │
│      - Price prediction models                              │
│      - Experiment tracking, model registry                  │
│                                                              │
│  CONSUMPTION LAYER (Power BI)                               │
│  └─→ Interactive dashboard with DAX measures                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

### Medallion Data Pipeline
- **Bronze**: Raw immutable storage
- **Silver**: Cleaned, validated data
- **Gold**: Business-ready aggregated features

### MLflow Integration
- **Experiment Tracking**: Model performance across runs
- **Model Registry**: Versioned model storage
- **Metrics**: R², MAE, RMSE tracking

### Power BI Dashboard
- **Price Trends**: Historical price visualization
- **Volume Analysis**: Trading volume correlations
- **Risk Metrics**: Volatility and drawdown analysis
- **ML Predictions**: Model forecasts overlay

---

## 📊 Results & Metrics

| Metric | Value |
| :--- | :--- |
| **Architecture** | Bronze → Silver → Gold (Medallion) |
| **ML Model** | Linear Regression (MLflow tracked) |
| **Key Features** | Price, volatility, volume correlations |
| **Dashboard** | Power BI with DAX measures |

---

## 📁 Project Structure

```
Crypto_Medallion_Analytics/
├── data/                              # Raw and processed data
├── pyspark/                           # PySpark ETL notebooks
│   ├── bronze_ingestion.py
│   ├── silver_transformation.py
│   └── gold_aggregation.py
├── ml/                                # Machine learning code
│   ├── train_model.py
│   └── mlflow_tracking.py
├── power_bi/                          # Power BI reports
├── img/                               # Dashboard screenshots
└── README.md                          # Project documentation
```

---

## 🔧 Setup & Installation

### Prerequisites
- Microsoft Fabric capacity (F64 or higher)
- Power BI Desktop (latest version)
- Fabric workspace permissions

### Deployment Steps

```bash
# Clone the repository
git clone https://github.com/Nicolenki7/Crypto_Medallion_Analytics.git
cd Crypto_Medallion_Analytics

# 1. Create Fabric Workspace
# 2. Run PySpark notebooks for Bronze/Silver/Gold layers
# 3. Configure MLflow tracking
# 4. Train ML models
# 5. Import Power BI report
# 6. Configure DAX measures
```

---

## 📈 Usage

### Dashboard Features

| Visualization | Purpose |
| :--- | :--- |
| **Price Trends** | Historical price movements |
| **Volume Correlation** | Price vs trading volume |
| **Volatility Analysis** | Risk metrics over time |
| **ML Predictions** | Model forecasts |

### Key Metrics
- **Precio_Inicio_Mes**: Month opening price
- **Precio_Fin_Mes**: Month closing price
- **Volatilidad_Media_Mensual**: Average monthly volatility
- **Volumen_Promedio_Mensual**: Average monthly volume

---

## 🎯 Key Learnings

- **Medallion Architecture** provides clear data quality boundaries
- **MLflow integration** enables reproducible ML experiments
- **Volume-backed analysis** filters false price signals
- **Power BI + Fabric** enables seamless analytics workflow

---

## 🔮 Future Enhancements

- [ ] Real-time crypto API ingestion
- [ ] Advanced ML models (LSTM, Prophet for time series)
- [ ] Multi-asset correlation analysis
- [ ] Automated retraining pipeline
- [ ] Alert system for price anomalies

---

## 🔗 Links

| Resource | URL |
| :--- | :--- |
| **Repository** | https://github.com/Nicolenki7/Crypto_Medallion_Analytics |
| **Live Dashboard** | [View in Fabric](https://app.fabric.microsoft.com/reportEmbed?reportId=ef628e11-1d49-421b-8a9d-b82867bf8d37) |
| **Related Project** | [Crypto Medallion ML App](https://github.com/Nicolenki7/crypto-medallion-ml-app) |

---

## 📝 Resumen en Español

Pipeline completo de datos implementando arquitectura **Medallion (Bronze → Silver → Gold)** para análisis de mercado de criptomonedas con modelos predictivos de ML.

Construido en Microsoft Fabric con ETL PySpark, tracking MLflow, y visualización Power BI. Incluye análisis de correlación riesgo/volumen y validación de tendencias respaldadas por volumen.

---

## 📄 License

MIT License — Feel free to fork, modify, and use for personal or commercial projects.

---

## 👤 Author

**Nicolás Zalazar** | Senior Data Engineer & Microsoft Fabric Specialist

- GitHub: [@Nicolenki7](https://github.com/Nicolenki7)
- LinkedIn: [nicolas-zalazar-63340923a](https://www.linkedin.com/in/nicolas-zalazar-63340923a)
- Portfolio: [nicolenki7.github.io/Portfolio](https://nicolenki7.github.io/Portfolio/)
- Email: zalazarn046@gmail.com

---

*Last Updated: March 2026*
