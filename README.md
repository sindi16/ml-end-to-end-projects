# 📘 Smartphone Dataset Analysis — README

## 📊 Project Overview
This notebook explores the Global Mobile Prices 2025 dataset.  
The goal is to understand how different smartphone features influence the final price, and to present findings using a clear single-page dashboard with multiple plot types.

The project includes:
- Data loading & preprocessing  
- Exploratory Data Analysis (EDA)  
- Visualizations of key relationships  
- A summary dashboard combining different plot types  
- Insights and conclusions  

---

## 📁 Dataset Description
The dataset contains smartphone specifications with their corresponding prices.

Main columns analyzed:
- **ram_gb** — RAM capacity  
- **storage_gb** — Internal storage  
- **camera_mp** — Camera resolution  
- **battery_mah** — Battery capacity  
- **display_size_inch** — Screen size  
- **price_usd** — Market price  
- **release_month** — Month the phone was released (if available)

---

## 🧪 Exploratory Steps
The notebook performs several EDA steps, including:

### ✔️ Descriptive statistics
Understanding distribution, ranges, and spread of numerical features.

### ✔️ Visual analysis of feature impact on price
Using scatterplots, line plots, histograms, and boxplots.

### ✔️ Correlation observations
Understanding linear relationships toward price.

---

## 📊 Summary Dashboard (Main Requirement)
A single-page dashboard was created to show the main “lines” of the dataset in one combined figure.

It includes:
- Price Distribution (Histogram)  
- Price Distribution (Boxplot)  
- Average Price by Release Month (Line Plot)  
- RAM vs Price (Scatter Plot)  
- Battery Capacity vs Price (Line Plot)  
- Camera Megapixels Distribution (Histogram)

This dashboard serves as a visual summary of the dataset’s key relationships.

---

## 🔍 Key Insights
- Price shows wide variability with noticeable outliers.  
- RAM and Storage have slight increasing trends with price but not strong correlations.  
- Camera MP & Battery show low direct correlation to price.  
- Release month does not appear to strongly affect pricing.  
- Overall, price is not strongly determined by single features alone, indicating possible non-linear or multi-factor relationships.


