# Food Delivery Time Analysis

## Project Overview
This project focuses on analyzing food delivery data to understand the factors that may affect delivery time, such as distance, weather conditions, road traffic density, and the number of deliveries.

The project also includes an interactive dashboard built using Streamlit, allowing users to explore the data, view analysis results, and estimate delivery time based on selected conditions.

## Problem
Delivery time can vary depending on several factors, making it difficult to estimate how long an order will take.

The goal of this project is to explore these factors, understand their relationship with delivery time, and present the findings through an interactive dashboard.

## Dataset
The dataset contains food delivery records and information about:

- Delivery person details
- Restaurant and delivery location coordinates
- Order date and time
- Weather conditions
- Road traffic density
- Vehicle condition
- Type of order and vehicle
- Number of deliveries
- Delivery time

## Data Cleaning and Analysis
The project included:

- Exploring the dataset and understanding its columns
- Handling missing values
- Checking incorrect and unusual values
- Investigating location coordinates and calculated distances
- Creating new features for analysis
- Exploring the relationship between different factors and delivery time
- Visualizing the findings

## Key Findings
The analysis showed that:

- Road traffic density is related to delivery time, with higher traffic generally associated with longer delivery times.
- The number of deliveries can affect the time required to complete an order.
- Distance is an important factor related to delivery time.
- Weather conditions may also contribute to differences in delivery time.

## Dashboard

An interactive dashboard was built using Streamlit and includes:

- **Overview:** Summary metrics and interactive filters.
- **Insights:** Charts, key findings, and recommendations.
- **Product:** A delivery time estimation tool based on selected conditions.

🔗 **Live Dashboard:**  
https://food-delivery-analysis-5tsuvqk4ovgpj7gpeuhymb.streamlit.app/

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/anux9/food-delivery-analysis.git
```

2. Navigate to the project folder:

```bash
cd food-delivery-analysis
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the dashboard:

```bash
streamlit run app.py
```

## Project Files

- `Project_Notebook_.ipynb` – Data cleaning, exploration, and analysis.
- `app.py` – Streamlit dashboard application.
- `clean.csv` – Cleaned dataset used by the project.
- `requirements.txt` – Required Python libraries.

## Conclusion

This project helped me apply the data analysis process in a practical way, starting with data cleaning and exploration, followed by analyzing the factors related to delivery time and presenting the findings through an interactive dashboard.
