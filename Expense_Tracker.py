expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    print("✅ Expense added!")

def view_expenses():
    print("\n💰 All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} - ₹{exp['amount']}")

def total_by_category(category):
    total = sum(exp["amount"] for exp in expenses if exp["category"] == category)
    print(f" Total for {category}: ₹{total}")

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total by Category")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        amt = float(input("Enter amount: "))
        cat = input("Enter category (Food/Travel/etc): ")
        add_expense(amt, cat)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        cat = input("Enter category: ")
        total_by_category(cat)
    elif choice == "4":
        break
    else:
        print("❌ Invalid choice!")
