# Electric Vehicle Market Segmentation Analysis in India - [Feynn Labs](https://www.linkedin.com/company/feynn-labs/?originalSubdomain=in) [Internship](https://feynnlabs.com/internships/)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Introduction

This project aims to segment the EV market in India. We will use a variety of methods, including market research, customer surveys, and statistical analysis. The goal of the project is to identify the different segments of the EV market and understand their needs and preferences. This information will be used to develop strategies to target these segments and grow the EV market in India.

- Electric Vehicle Market Segmentation Analysis  -  jupyter notebook [link](main.ipynb) 
- Dataset [link](dataset)
- Dataset Splitup [link](dataset%20splitup)
- Final report [link](reports)

## Team members
|Name|GitHub repo link|
|--|--|
|Adhiban Siddarth ![Me](https://img.shields.io/badge/Me-green) ![Team Lead](https://img.shields.io/badge/Team_Lead-red) | [![GitHub Link](https://img.shields.io/badge/GitHub-Link-blue?logo=github&logoColor=white)](https://github.com/Adhiban1/EV-Market-Segmentation) |
|Karakavalasa venkata pranay | [![GitHub Link](https://img.shields.io/badge/GitHub-Link-blue?logo=github&logoColor=white)](https://github.com/Venkatapranay/electronicvehicles) |
|Malay Vyas | [![GitHub Link](https://img.shields.io/badge/GitHub-Link-blue?logo=github&logoColor=white)](https://github.com/MalayVyas/EV_Market/) |
|Shreyash Banduji Chacharkar | [![GitHub Link](https://img.shields.io/badge/GitHub-Link-blue?logo=github&logoColor=white)](https://github.com/ShreyashChacharkar/EV_marketsegment) |
|Yash Mayur | [![GitHub Link](https://img.shields.io/badge/GitHub-Link-blue?logo=github&logoColor=white)](https://github.com/ysmayur1992/Feyyn_Labs_Project_3) |

## Workflow

|Date|What to do|
|--|--|
|Aug 31 - Sep 2|Project Kick-off and Data Collection|
|Sep 3 - Sep 4|Intensive Data Collection and Research|
|Sep 5 - Sep 7|Data Analysis|
|Sep 8 - Sep 9|Market Segmentation|
|Sep 10 - Sep 11|Segment Profiling|
|Sep 12 - Sep 13|Strategy Outline|
|Sep 14|Submission|

## dataset and files

Each teammate should collect atleast 2 dataset.

```
├── dataset
├── files
```

- **dataset**: contains csv files
- **files**: contains other file formats like pdf

```
dataset
├── Adhiban
│   └── *.csv
├── Malay
│   └── *.csv
├── Pranay
│   └── *.csv
├── Shreyash
│   └── *.csv
└── Yash
    └── *.csv
15 directories, 33 files
```

## Dataset splitup

[dataset splitup](dataset%20splitup)

|Dataset|No of cells|Selected by|
|--|--|--|
|1|125877|Pranay|
|2|113700|Adhiban|
|3|112171|Yash|
|4|1915898|Malay|
|5|1551717|Shreyash|

## Final report
Final report is the combination all our reports.

[Final report pdf link](reports/Team-Adhiban.pdf)

## Car Price Prediction

Flask App:

```
pip install flask scikit-learn
```

```
python app.py
```

[![Docker image](https://img.shields.io/badge/Docker_image-Link-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=%230db7ed.svg)](https://hub.docker.com/r/adhiban/car-price)

Docker pull:

```
docker pull adhiban/car-price
```

Docker run:

```
docker run -p 5000:5000 adhiban/car-price
```