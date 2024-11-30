import streamlit as st

# List to hold the expenses
expenses = []

# Function to add an expense
def add_expense(description, category, amount, date):
    """Function to add an expense"""
    expense = {
        'description': description,
        'category': category,
        'amount': amount,
        'date': date
    }
    expenses.append(expense)

# Function to display all expenses
def view_expenses():
    """Function to view all expenses"""
    if not expenses:
        st.write("No expenses recorded.")
        return
    
    st.write("### All Expenses")
    for expense in expenses:
        st.write(f"**Description:** {expense['description']}")
        st.write(f"**Category:** {expense['category']}")
        st.write(f"**Amount:** ${expense['amount']}")
        st.write(f"**Date:** {expense['date']}")
        st.write("---")

# Function to view expenses by category
def view_expenses_by_category(category):
    """Function to view expenses by category"""
    category_expenses = [expense for expense in expenses if expense['category'].lower() == category.lower()]

    if not category_expenses:
        st.write(f"No expenses found for category: {category}")
        return

    st.write(f"### Expenses for {category}")
    for expense in category_expenses:
        st.write(f"**Description:** {expense['description']}")
        st.write(f"**Amount:** ${expense['amount']}")
        st.write(f"**Date:** {expense['date']}")
        st.write("---")

# Function to calculate and show the total expenses
def total_expenses():
    """Function to calculate and show the total expenses"""
    total = sum(expense['amount'] for expense in expenses)
    st.write(f"### Total Expenses: ${total:.2f}")

# Streamlit UI Elements
st.title("Expense Tracker")

# Sidebar for navigation
option = st.sidebar.selectbox("Choose an option", ["Add Expense", "View All Expenses", "View Expenses by Category", "View Total Expenses"])

if option == "Add Expense":
    st.subheader("Enter Expense Details")
    description = st.text_input("Description")
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.01, format="%.2f")
    date = st.date_input("Date")

    if st.button("Add Expense"):
        add_expense(description, category, amount, date)
        st.success("Expense added successfully!")

elif option == "View All Expenses":
    view_expenses()

elif option == "View Expenses by Category":
    category = st.text_input("Enter category to filter by:")
    if category:
        view_expenses_by_category(category)

elif option == "View Total Expenses":
    total_expenses()

