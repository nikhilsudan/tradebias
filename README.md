# TradeBias 🧠📊  
*A behavioral analytics tool to detect psychological trading biases from trade logs.*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/your-username/TradeBias)

---

## 📌 Overview  
Traders often lose money not because of lack of strategy, but because of **behavioral biases** such as **FOMO, revenge trading, and overtrading**.  
**TradeBias** is a Python-based tool that analyzes CSV trade logs to detect such patterns and generate insightful reports.  

This project highlights skills in **data cleaning, analysis, visualization, and behavioral finance logic** — making it both practical and resume-worthy.  

---

## 🚀 Features  
- 📂 Import trade logs in CSV format  
- 🔍 Detect common trading biases:
  - Fear of Missing Out (FOMO)  
  - Revenge Trading  
  - Overtrading  
  - Loss Aversion (optional extension)  
- 📊 Generate summary statistics  
- 📑 Export results as a clean, human-readable report  
- 💡 Modular & extensible design  

---

## 🛠️ Tech Stack  
- **Python** (Pandas, NumPy)  
- **Matplotlib / Seaborn** (for visualizations)  
- **Jupyter Notebook** (for experimentation & prototyping)  

---

## 📂 Project Structure  


tradebias_ai/
├── data/
│ ├── raw/ # Raw input trade data (CSV files)
│ └── processed/ # Processed / cleaned trade reports
├── notebooks/ # Jupyter notebooks for EDA & visuals
├── src/ # Core Python code (package)
│ ├── init.py
│ ├── bias_detector.py
│ ├── generate_synthetic.py
│ ├── tradebias.py
│ └── main.py
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── LICENSE # MIT License

---

## ⚡ Getting Started  

To set up and run TradeBias locally:  

```bash
# 1. Clone the repository
git clone https://github.com/your-username/TradeBias.git
cd TradeBias

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis on a sample trade log
python -m tradebias.analyzer data/sample_trades.csv

---


