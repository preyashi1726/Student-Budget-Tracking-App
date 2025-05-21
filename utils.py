# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 13:42:54 2025

@author: DELL
"""

import os
import pandas as pd
# File paths
USERS_FILE = 'data/users1.csv'
EXPENSES_FILE = 'data/expenses1.csv'

def load_user_data():
    """Load user data from CSV file or create empty dataframe if file doesn't exist"""
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    else:
        columns = ["Name", "Password", "Age", "Gender", "Student_Accommodation", 
                   "Utilities", "Grocery_shopping", "Takeaways/dining", 
                   "Public_Transportation", "Tuition_Fees", "Books_and_Supplies",
                   "Clothing", "Entertainment", "Health/Medical_Expenses", "Monthly_Income"]
        return pd.DataFrame(columns=columns)
    

def save_user_data(users_df):
    """Save user data to CSV file"""
    users_df.to_csv(USERS_FILE, index=False)

def load_expense_data():
    """Load expense data from CSV file or create empty dataframe if file doesn't exist"""
    if os.path.exists(EXPENSES_FILE):
        return pd.read_csv(EXPENSES_FILE)
    else:
        # Create empty dataframe with required columns
        columns = ["Username", "Category", "Amount", "Date", "Note"]
        return pd.DataFrame(columns=columns)

def save_expense_data(expenses_df):
    """Save expense data to CSV file"""
    expenses_df.to_csv(EXPENSES_FILE, index=False)

def get_user_expenses(expenses_df, username):
    """Get expenses for a specific user"""
    return expenses_df[expenses_df['Username'] == username].copy()

def calculate_expense_metrics(user_data, user_expenses):
    """Calculate expense metrics for dashboard"""
    # Calculate total expenses from user expenses
    if user_expenses.empty:
        total_expenses = 0
        expense_by_category = pd.DataFrame(columns=['Category', 'Amount'])
    else:
        total_expenses = user_expenses['Amount'].sum()
        expense_by_category = user_expenses.groupby('Category')['Amount'].sum().reset_index()
   
    # Get income
    income = user_data['Monthly_Income']
   
    # Calculate savings
    savings = income - total_expenses
   
    # Calculate expense ratio (% of income spent)
    expense_ratio = (total_expenses / income * 100) if income > 0 else 0
   
    return total_expenses, expense_by_category, income, savings, expense_ratio

