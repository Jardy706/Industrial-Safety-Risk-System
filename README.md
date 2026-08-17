# Industrial-Safety-Risk-System
# Industrial Safety Risk Assessment System


## Overview

This project develops a Python-based industrial safety risk assessment system using weighted risk scoring.


## Motivation

Industrial accidents are often related to multiple risk factors.
This project aims to build a simple computational framework for evaluating safety risks.


## Methodology

The risk score is calculated based on:

- Temperature
- Pressure
- Worker experience


Formula:

Risk Score =
Temperature × 0.4
+
Pressure × 0.4
+
Worker Experience × 0.2


## Features

- Risk score calculation
- Automatic risk classification
- Structured safety data representation

## Example Output

Input:

Temperature:95
Pressure:85
Experience:60


Output:

Risk Score: 84

Status: Danger

## Technology

Python

## Project Structure
```text
Industrial-Safety-Risk-System
│
├── risk_system.py
├── README.md
└── .gitignore
```
## Future Improvements

- Integrate real-world safety datasets
- Apply machine learning models
- Develop AI-based risk prediction systems
