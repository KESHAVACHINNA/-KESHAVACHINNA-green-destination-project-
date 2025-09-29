# Task 1: Cyclone Machine Data Analysis

## 1. Project Description

[cite_start]This project involves a comprehensive analysis of a 3-year time-series dataset from cyclone machine sensors[cite: 7]. The primary objectives are to:
* [cite_start]Clean and prepare the sensor data for analysis[cite: 17].
* [cite_start]Programmatically detect machine shutdown/idle periods[cite: 21].
* [cite_start]Segment the machine's active time into distinct operational states using clustering[cite: 26].
* [cite_start]Identify contextual anomalies within each operational state and hypothesize their root causes[cite: 32, 36].
* [cite_start]Build and evaluate a short-horizon model to forecast the `Cyclone_Inlet_Gas_Temp`[cite: 42].

## 2. Folder Structure

The final folder is organized as follows:

```
Task1/
├── plots/
│   ├── (Generated plot images, e.g., anomaly_plot.png)
│
├── anomalous_periods.csv
├── clusters_summary.csv
├── forecasts.csv
├── shutdown_periods.csv
├── task1_analysis.ipynb
└── README.md
```

## 3. Setup and Installation

To run this analysis, please ensure you have Python 3.8+ and the required libraries installed.

**Step 1: Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Step 2: Install Dependencies**
A `requirements.txt` file should be provided. Install the necessary libraries using pip:
```bash
pip install -r requirements.txt
```
*(Note: If you are creating this project, you can generate the `requirements.txt` file after installing your libraries by running `pip freeze > requirements.txt`)*

**Key libraries used:**
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* statsmodels
* (Add any other libraries you used)

## 4. How to Run the Analysis

1.  Ensure your environment is set up and all libraries are installed as described in Section 3.
2.  Place the raw dataset file (e.g., `cyclone_data.csv`) in the root of the `Task1` folder.
3.  Open and run the Jupyter Notebook **`task1_analysis.ipynb`** from top to bottom.
4.  [cite_start]The script will perform the full analysis and automatically generate all required output files: the four CSVs will be saved in the root `Task1` directory [cite: 54][cite_start], and all plots will be saved in the `plots/` directory[cite: 59].

## 5. Description of Files

* [cite_start]**`task1_analysis.ipynb`**: The main Jupyter Notebook containing all the Python code for data preparation, analysis, clustering, anomaly detection, and forecasting[cite: 53].
* [cite_start]**`plots/`**: This directory contains all visualizations generated during the analysis, saved as PNG files[cite: 59].
* [cite_start]**`shutdown_periods.csv`**: Contains the start time, end time, and duration of all detected machine shutdown periods[cite: 55].
* [cite_start]**`anomalous_periods.csv`**: Lists all detected anomalies with associated metadata such as timing, duration, implicated variables, and the machine state in which they occurred[cite: 56].
* [cite_start]**`clusters_summary.csv`**: Provides summary statistics (mean, std, etc.) for each identified operational machine state (cluster)[cite: 57].
* [cite_start]**`forecasts.csv`**: Contains the true vs. predicted values from the time-series forecasting model for the held-out test set[cite: 58].
* [cite_start]**`README.md`**: This file, providing an overview and instructions for the project[cite: 60].
