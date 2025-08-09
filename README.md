# AUTOMATED-REPORT-GENERATION

# COMPANY: CODTECH IT SOLUTIONS 

# NAME: Bhushan satyavan waghmare

# INTERN ID: CT04DH2105

# DOMAIN: PYTHON

# DURATION: 4 weeks

# MENTOR: NEELA SANTOSH


---

# 📊 Sales Report Generator

## 📌 Overview

This project is a **Python script** that reads sales data from a CSV file, analyzes it, and generates a **PDF report** with:

* **Total Sales**
* **Average Sales**
* **Maximum Sale Value**
* **Detailed Product Sales Table**

It uses the **FPDF** library for creating the PDF file in a clean, tabular format.

---

## 🗂 Project Structure

```
.
├── generate_report.py   # Main Python script
├── sales_data.csv       # Input sales data file (CSV format)
├── sales_report.pdf     # Generated PDF report
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

1. **Read CSV File**

   * Reads product name, units sold, and price per unit from `sales_data.csv`.

2. **Analyze Data**

   * Calculates:

     * **Total Sales** (units × price, summed across all products)
     * **Average Sales** per product
     * **Maximum Sale Value**

3. **Generate PDF Report**

   * Creates a **Sales Report** with:

     * Summary statistics (Total, Average, Max)
     * A detailed table of product sales

---

## 🛠 Requirements

Make sure you have the following installed:

* **Python 3.x**
* **pip** (Python package manager)

Python Libraries:

```txt
fpdf==1.7.2
```

Install all requirements:

```bash
pip install -r requirements.txt
```

Example `requirements.txt` file:

```
fpdf==1.7.2
```

---

## 🚀 How to Run

1. **Install Requirements**

   ```bash
   pip install fpdf
   ```

   Or using the requirements file:

   ```bash
   pip install -r requirements.txt
   ```
2. **Prepare CSV File** (`sales_data.csv`)
   Format:

   ```
   Product,Units Sold,Price
   Product A,10,15.5
   Product B,8,12.0
   Product C,20,7.5
   ```
3. **Run Script**

   ```bash
   python generate_report.py
   ```
4. **Check Output**

   * The PDF report will be saved as **`sales_report.pdf`** in the project folder.

---

## 📊 Example Output in PDF

```
Sales Report
Total Sales: $500.00
Average Sales: $166.67
Max Sale: $200.00

| Product   | Units Sold | Price |
|-----------|------------|-------|
| Product A | 10         | 15.5  |
| Product B | 8          | 12.0  |
| Product C | 20         | 7.5   |
```

---

## ✨ Features

* Reads and processes CSV sales data.
* Generates a **clean PDF report**.
* Displays summary and detailed tables.
* Easy to customize and expand.

---
If you want, I can also add a code block in README that shows a sample data.csv so users can test your script immediately. Would you like me to do that?


