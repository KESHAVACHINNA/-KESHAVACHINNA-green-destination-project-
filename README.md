# Task 1: Cyclone Machine Data Analysis – README
1. Project Overview

This project provides an end-to-end analysis of a 3-year time-series dataset from a cyclone machine. The workflow includes:

Data cleaning and exploratory analysis

Shutdown and idle period detection

Machine state segmentation (clustering)

Contextual anomaly detection and root cause analysis

Short-horizon forecasting

Insights synthesis and actionable recommendations

The goal is to detect operational patterns, predict potential issues, and provide recommendations to improve reliability and efficiency.

2. Folder Structure
Task1/
├── task1_analysis.ipynb         # Main analysis notebook (or .py script)
├── shutdown_periods.csv         # Detected shutdown periods
├── clusters_summary.csv         # Summary statistics for each machine state
├── anomalous_periods.csv        # List of anomalies with metadata
├── forecasts.csv                # True vs predicted values for forecasting
├── plots/                       # All generated plots (PNG format)
└── README.md                    # This file

3. Environment Setup

Python version: 3.9+

Recommended: Use a virtual environment

Install dependencies:

pip install -r requirements.txt


Required Python libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, pmdarima, statsmodels, hdbscan (optional for advanced clustering)

4. How to Run the Analysis
Step 1: Data Preparation & Exploratory Analysis

Purpose: Load and clean the raw data, handle missing values, ensure strict 5-minute intervals, compute summary statistics, and visualize patterns.

Run: Execute the cells under "Data Preparation & Exploratory Analysis".

Step 2: Shutdown / Idle Period Detection

Purpose: Identify periods when the machine was idle or shut down. Compute total downtime and number of shutdown events.

Run: Execute "Shutdown / Idle Period Detection" section.

Output: shutdown_periods.csv and plots highlighting shutdown periods.

Step 3: Machine State Segmentation (Clustering)

Purpose: Cluster operational data into interpretable states (e.g., Normal, High Load). Generate summary statistics for each state.

Run: Execute "Machine State Segmentation" section.

Output: clusters_summary.csv and state visualizations in plots/.

Step 4: Contextual Anomaly Detection + Root Cause Analysis

Purpose: Detect anomalies relative to operational states. Provide root cause hypotheses for selected events with visualizations.

Run: Execute "Contextual Anomaly Detection" section.

Output: anomalous_periods.csv and anomaly plots in plots/.

Step 5: Short-Horizon Forecasting

Purpose: Forecast Cyclone_Inlet_Gas_Temp for the next 1 hour (12 steps) using multiple models. Evaluate using RMSE and MAE.

Run: Execute "Short-Horizon Forecasting" section.

Output: forecasts.csv and forecast plots in plots/.

Step 6: Insights & Storytelling

Purpose: Synthesize results from all previous steps to provide key insights and actionable recommendations.

Run: Execute "Insights & Storytelling" section. No separate file output; results are shown in the notebook.

5. Output Files Summary
File	Description
task1_analysis.ipynb	Main analysis notebook
shutdown_periods.csv	Detected shutdown periods (start, end, duration)
clusters_summary.csv	Summary statistics and descriptions of operational states
anomalous_periods.csv	Consolidated list of anomalies with timestamps, duration, variables, and state
forecasts.csv	True vs predicted values for forecasting task
plots/	All visualizations (shutdowns, clusters, anomalies, forecasts)
