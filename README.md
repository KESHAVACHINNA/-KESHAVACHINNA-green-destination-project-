# Project: Cyclone Machine Analysis & RAG System

## 1. Project Overview

This submission contains two distinct but related data science tasks:

* **Task 1: Machine Data Analysis**: A deep dive into a 3-year time-series dataset from cyclone machine sensors. The analysis focuses on detecting shutdowns, identifying operational states through clustering, finding contextual anomalies, and forecasting future sensor values.
* **Task 2: RAG + LLM System Design**: A design and prototype for a Retrieval-Augmented Generation (RAG) system. This system is designed to answer natural language questions about technical documents using open-source language models.

This document provides instructions on how to run the code for both tasks and describes the contents of each deliverable file.

---

## 2. Instructions on Running the Code

### Task 1: Machine Data Analysis

1.  **Navigate** to the `/Task1/` directory.
2.  **Set up the environment**: Create a Python virtual environment and install the required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute the code**: Open and run the Jupyter Notebook `task1_analysis.ipynb` cell by cell. The notebook is designed to run end-to-end and will generate all the necessary CSV outputs and plots.

### Task 2: RAG System Prototype

1.  **Navigate** to the `/Task2/prototype/` directory.
2.  **Set up the environment**: Install the required packages using the `requirements.txt` file located in this directory.
    ```bash
    pip install -r requirements.txt
    ```
3.  **Download models**: The code may require downloading open-source embedding and language models from Hugging Face. The script will handle this, but an active internet connection is needed for the first run.
4.  **Run the prototype**: Execute the prototype script from your terminal.
    ```bash
    python rag_prototype.py
    ```

---

## 3. Description of Deliverables

### Final Presentation

* [cite_start]**`Final_Presentation.pptx`**: A 6-9 slide presentation summarizing the methodology, findings, and system design for both tasks[cite: 113, 114].

### Task 1 Deliverables (located in `/Task1/`)

* [cite_start]**`task1_analysis.ipynb`**: The main Jupyter Notebook containing all code for the time-series analysis[cite: 53].
* [cite_start]**`/plots/`**: A folder containing all visualizations generated during the analysis, saved as PNG files[cite: 59].
* [cite_start]**`shutdown_periods.csv`**: A CSV file listing all detected machine shutdowns with their start, end, and duration[cite: 55].
* [cite_start]**`anomalous_periods.csv`**: Contains the list of detected anomalies with relevant metadata[cite: 56].
* [cite_start]**`clusters_summary.csv`**: A summary of the statistics for each identified operational state[cite: 57].
* [cite_start]**`forecasts.csv`**: The true vs. predicted values from the forecasting models[cite: 58].

### Task 2 Deliverables (located in `/Task2/`)

* [cite_start]**`architecture_diagram.pptx`**: A slide or image illustrating the complete RAG system architecture[cite: 104].
* [cite_start]**`notes.md`**: A markdown file detailing design choices, the retrieval strategy, guardrails, and the scalability plan[cite: 105].
* [cite_start]**`/prototype/`**: A folder containing the minimal, runnable RAG prototype code (`rag_prototype.py`), sample documents, and its own README with specific run steps[cite: 106, 107, 108, 109].
