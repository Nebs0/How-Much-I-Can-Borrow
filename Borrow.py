#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:12:24 2023

@author: nebiyousamuel
"""

def calculate_loan_amount(payment, interest_rate, months):
    # Convert the interest rate from percentage to decimal
    r = interest_rate / 100.0

    # Calculate the loan amount (present value, Pv)
    loan_amount = (1 - (1 + r) ** (-months)) * payment / r

    return loan_amount

def main():
    try:
        payment = float(input("Enter the monthly payment amount: $"))
        interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        months = int(input("Enter the number of months for the loan: "))

        loan_amount = calculate_loan_amount(payment, interest_rate, months)

        print(f"You can afford to borrow: ${loan_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
