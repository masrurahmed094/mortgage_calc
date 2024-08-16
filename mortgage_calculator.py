import tkinter as tk
from tkinter import ttk, messagebox

def calculate_loan():
    try:
        principal = float(entry_principal.get()) if entry_principal.get() else 0
        annual_rate = float(entry_rate.get()) if entry_rate.get() else 0
        years = int(entry_years.get()) if entry_years.get() else 1
        monthly_income = float(entry_income.get()) if entry_income.get() else 1

        loan_type = loan_type_var.get()
        monthly_rate = annual_rate / 12 / 100 if annual_rate else 0
        n_payments = years * 12
        monthly_payment = (principal * (monthly_rate * (1 + monthly_rate) ** n_payments) / ((1 + monthly_rate) ** n_payments - 1)) if monthly_rate else 0

        total_interest = monthly_payment * n_payments - principal
        
        if loan_type == "Mortgage":
            tax_rate = float(entry_tax.get()) if entry_tax.get() else 0
            insurance_cost = float(entry_insurance.get()) if entry_insurance.get() else 0
            monthly_taxes = (principal * tax_rate / 100) / 12 if tax_rate else 0
            total_monthly_payment = monthly_payment + monthly_taxes + insurance_cost
        else:
            total_monthly_payment = monthly_payment

        income_percentage = (total_monthly_payment / monthly_income) * 100 if monthly_income else 0

        label_result.config(text=f"Monthly Payment: ${total_monthly_payment:.2f}\n"
                                 f"Total Interest Paid: ${total_interest:.2f}\n"
                                 f"Income Percentage: {income_percentage:.2f}%")
        
        if income_percentage > 28:
            label_advice.config(text="Warning: Above 28% of income!")
        else:
            label_advice.config(text="This loan is affordable.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values or leave the field empty.")

def update_fields(*args):
    loan_type = loan_type_var.get()
    if loan_type == "Mortgage":
        label_tax.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        entry_tax.grid(row=5, column=1, padx=5, pady=5)
        label_insurance.grid(row=6, column=0, sticky="e", padx=5, pady=5)
        entry_insurance.grid(row=6, column=1, padx=5, pady=5)
    else:
        label_tax.grid_remove()
        entry_tax.grid_remove()
        label_insurance.grid_remove()
        entry_insurance.grid_remove()

# Create the main window
root = tk.Tk()
root.title("Loan Affordability Calculator")

# Set window dimensions and configure the grid to center content
root.geometry("600x400")
root.configure(bg="#333333")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Loan Type Selection
tk.Label(root, text="Select Loan Type:", bg="#333333", fg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
loan_type_var = tk.StringVar(value="Mortgage")
loan_type_var.trace("w", update_fields)
loan_type_menu = ttk.Combobox(root, textvariable=loan_type_var, values=["Mortgage", "Auto Loan", "Personal Loan", "Student Loan"])
loan_type_menu.grid(row=1, column=1, padx=5, pady=5)

# Create input fields
tk.Label(root, text="Loan Amount ($):", bg="#333333", fg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_principal = tk.Entry(root)
entry_principal.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Annual Interest Rate (%):", bg="#333333", fg="white").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Loan Term (years):", bg="#333333", fg="white").grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_years = tk.Entry(root)
entry_years.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Monthly Income ($):", bg="#333333", fg="white").grid(row=5, column=0, sticky="e", padx=5, pady=5)
entry_income = tk.Entry(root)
entry_income.grid(row=5, column=1, padx=5, pady=5)

# Mortgage specific fields
label_tax = tk.Label(root, text="Property Tax Rate (%):", bg="#333333", fg="white")
entry_tax = tk.Entry(root)
label_insurance = tk.Label(root, text="Monthly Insurance ($):", bg="#333333", fg="white")
entry_insurance = tk.Entry(root)

# Create buttons
calculate_btn = tk.Button(root, text="Calculate", command=calculate_loan, bg="#444444", fg="white")
calculate_btn.grid(row=7, column=1, padx=5, pady=10, sticky="w")
reset_btn = tk.Button(root, text="Reset", command=lambda: [entry_principal.delete(0, tk.END), entry_rate.delete(0, tk.END), 
                                                           entry_years.delete(0, tk.END), entry_income.delete(0, tk.END), 
                                                           entry_tax.delete(0, tk.END), entry_insurance.delete(0, tk.END),
                                                           label_result.config(text=""), label_advice.config(text="")],
                      bg="#444444", fg="white")
reset_btn.grid(row=7, column=1, padx=5, pady=10, sticky="e")

# Display results
label_result = tk.Label(root, text="", font=('Helvetica', 14), bg="#333333", fg="white")
label_result.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

label_advice = tk.Label(root, text="", font=('Helvetica', 12), fg='red', bg="#333333")
label_advice.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI loop
update_fields()
root.mainloop()
