# TradeBias 🧠📈
*A behavioral analytics tool for traders*

## Overview
TradeBias analyzes trading logs to detect **psychological biases** such as FOMO, revenge trading, overtrading, and emotional entries.  
It provides both **statistical summaries** and **visual insights** to help traders improve discipline and decision-making.

## Features
- Detects common trading biases from CSV logs  
- Generates synthetic trade data for testing  
- Produces statistical summaries (win rate, PnL, bias counts)  
- Visualizes results with bar charts & pie charts  
- Modular design for future integration with real trading platforms  

## Tech Stack
- **Python** (pandas, matplotlib, seaborn)  
- **Jupyter Notebooks** for visualization  
- **VSCode** for development  

## Project Structure
├── data
│ ├── raw/ # Raw CSV trade data
│ └── processed/ # Processed outputs
├── notebooks/ # Jupyter notebooks for exploration
├── src/ # Core project source code
│ ├── init.py
│ ├── bias_detector.py
│ ├── generate_synthetic.py
│ ├── tradebias.py
│ └── main.py
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore