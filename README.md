
# Task 1: Cyclone Machine Data Analysis - README

## 1. Project Overview

This project performs an end-to-end analysis of a 3-year time-series dataset from a cyclone machine. The analysis is broken down into six sequential parts, starting with data cleaning and culminating in actionable insights and recommendations. This document explains each analytical step and provides instructions on how to run the code.

---

## 2. General Instructions to Run the Code

1.  **Environment Setup**:
    * It is recommended to use a Python virtual environment.
    * Install all required libraries by running `pip install -r requirements.txt`.

2.  **Execution**:
    * The entire analysis is located in the **`task1_analysis.ipynb`** (or **`.py`**) file.
    * The code is designed to be run sequentially from top to bottom. Each numbered section in the notebook corresponds to the analytical steps described below.

---

## 3. Description of Analytical Steps & How to Run Each

### 1) Data Preparation & Exploratory Analysis

* **What it is**: This first step involves loading and cleaning the raw sensor data to make it suitable for analysis. [cite_start]It includes handling missing values, ensuring strict 5-minute time indexing, calculating summary statistics, and visualizing the data to understand its basic patterns[cite: 17, 18, 19].
* **How to run it**: Execute the cells under the "Data Preparation & Exploratory Analysis" section in the notebook. This will load the data, perform cleaning operations, and generate initial summary tables and plots.

### 2) Shutdown / Idle Period Detection

* [cite_start]**What it is**: This part programmatically detects and segments all periods when the machine was not operational[cite: 21]. [cite_start]The total downtime and number of shutdown events are computed, and a visualization is created to highlight these periods over a full year[cite: 22, 23].
* **How to run it**: Run the cells in the "Shutdown / Idle Period Detection" section. This will process the cleaned data, identify idle periods, and save the results to **`shutdown_periods.csv`**.

### 3) Machine State Segmentation (Clustering)

* [cite_start]**What it is**: Using the active operational data (shutdowns excluded), this step applies multivariate clustering to group the data into interpretable machine states like 'Normal', 'High Load', etc.[cite: 25, 26, 27]. [cite_start]For each state, summary statistics and descriptions are generated[cite: 28, 29, 30, 31].
* **How to run it**: Execute the cells under the "Machine State Segmentation" section. This will train the clustering model, assign state labels to the data, and save the state summaries to **`clusters_summary.csv`**.

### 4) Contextual Anomaly Detection + Root Cause Analysis

* [cite_start]**What it is**: This section focuses on building a system to detect anomalies that are contextual to each specific machine state[cite: 33]. [cite_start]It produces a list of anomalies and includes a root cause hypothesis for 3-6 selected events, supported by visualizations[cite: 35, 36, 40].
* **How to run it**: Run the cells in the "Contextual Anomaly Detection" section. This code will train the detection models, identify anomalies, and save them to **`anomalous_periods.csv`**.

### 5) Short-Horizon Forecasting

* [cite_start]**What it is**: The goal here is to forecast the `Cyclone_Inlet_Gas_Temp` for the next hour (12 steps)[cite: 42]. [cite_start]At least two different forecasting methods are built and compared, with their performance evaluated using RMSE and MAE[cite: 43, 44].
* **How to run it**: Execute the cells under the "Short-Horizon Forecasting" section. This will train the models, generate predictions on the test set, and save the results to **`forecasts.csv`**.

### 6) Insights & Storytelling

* [cite_start]**What it is**: This is the final part of the analysis, where all previous findings are connected to provide 3-5 concise insights and actionable recommendations[cite: 47, 49].
* **How to run it**: The cells in this section typically contain markdown and data aggregation code that synthesizes results from the previous steps. Running them will display the final summary and conclusions. There is no separate file output for this step.
