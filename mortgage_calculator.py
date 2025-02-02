from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox # type: ignore

def calculate_loan():
    try:
        principal = float(entry_principal.text()) if entry_principal.text() else 0
        annual_rate = float(entry_rate.text()) if entry_rate.text() else 0
        years = int(entry_years.text()) if entry_years.text() else 1
        monthly_income = float(entry_income.text()) if entry_income.text() else 1
        
        monthly_rate = annual_rate / 12 / 100 if annual_rate else 0
        n_payments = years * 12
        
        if monthly_rate:
            monthly_payment = (principal * (monthly_rate * (1 + monthly_rate) ** n_payments) /
                              ((1 + monthly_rate) ** n_payments - 1))
        else:
            monthly_payment = principal / n_payments if n_payments else 0

        total_interest = monthly_payment * n_payments - principal
        income_percentage = (monthly_payment / monthly_income) * 100 if monthly_income else 0
        
        result_label.setText(f"Monthly Payment: ${monthly_payment:.2f}\n"
                             f"Total Interest: ${total_interest:.2f}\n"
                             f"Income Percentage: {income_percentage:.2f}%")
        
        if income_percentage > 28:
            warning_label.setText("Warning: Above 28% of income!")
        else:
            warning_label.setText("Loan is affordable.")
    
    except ValueError:
        QMessageBox.critical(window, "Input Error", "Please enter valid numeric values.")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Loan Calculator")
layout = QVBoxLayout()

layout.addWidget(QLabel("Loan Amount ($):"))
entry_principal = QLineEdit()
layout.addWidget(entry_principal)

layout.addWidget(QLabel("Annual Interest Rate (%):"))
entry_rate = QLineEdit()
layout.addWidget(entry_rate)

layout.addWidget(QLabel("Loan Term (years):"))
entry_years = QLineEdit()
layout.addWidget(entry_years)

layout.addWidget(QLabel("Monthly Income ($):"))
entry_income = QLineEdit()
layout.addWidget(entry_income)

calculate_button = QPushButton("Calculate")
calculate_button.clicked.connect(calculate_loan)
layout.addWidget(calculate_button)

result_label = QLabel()
layout.addWidget(result_label)

warning_label = QLabel()
layout.addWidget(warning_label)

window.setLayout(layout)
window.show()
app.exec()
