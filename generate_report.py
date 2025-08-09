import csv
from fpdf import FPDF
import os

pdf_path = "sales_report.pdf"

if os.path.exists(pdf_path):
    print(f"PDF generated: {pdf_path}")
    os.startfile(pdf_path)
else:
    print("PDF file was not created.")


def analyze_data(file_path):
  
    total_sales = 0
    max_sale = 0
    sales_data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            sales_data.append(row)
            total_sales += float(row[1]) * float(row[2])
            if float(row[2]) > max_sale:
                max_sale = float(row[2])
    
    average_sales = total_sales / len(sales_data)

    return total_sales, average_sales, max_sale, sales_data


def generate_pdf_report(total_sales, average_sales, max_sale, sales_data):
   
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Sales Report", 0, 1, "C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Total Sales: ${total_sales:.2f}", 0, 1)
    pdf.cell(200, 10, f"Average Sales: ${average_sales:.2f}", 0, 1)
    pdf.cell(200, 10, f"Max Sale: ${max_sale:.2f}", 0, 1)
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(50, 10, "Product", 1)
    pdf.cell(50, 10, "Units Sold", 1)
    pdf.cell(50, 10, "Price", 1)
    pdf.ln()
    pdf.set_font("Arial", "", 12)
    for row in sales_data:
        pdf.cell(50, 10, row[0], 1)
        pdf.cell(50, 10, row[1], 1)
        pdf.cell(50, 10, row[2], 1)
        pdf.ln()
    pdf.output("sales_report.pdf")


if __name__ == "__main__":
    file_path = "sales_data.csv"
    report_data = analyze_data(file_path)
    total_sales, average_sales, max_sale, sales_data = analyze_data("sales_data.csv")
    generate_pdf_report(total_sales, average_sales, max_sale, sales_data)
