# 🚗 Swamiraj Renters — Car Rental System

A console-based **Car Rental System developed using Python** that allows eligible customers to explore available luxury cars, select a model, calculate rental costs, and find alternative vehicles that fit their budget.

The project demonstrates Python fundamentals through conditional statements, loops, dictionaries, lists, user input, and basic billing logic.

## ✨ Features

- **Customer Registration:** Collects the customer's name, age, and driving license status.
- **Eligibility Verification:** Checks whether the customer is at least 18 years old and has a driving license.
- **Multiple Car Brands:** Offers vehicles from BMW, Tesla, and Mercedes.
- **Model Selection:** Displays available car models with their daily rental charges and security deposits.
- **Rental Cost Calculation:** Calculates the total cost based on the rental duration and deposit.
- **Budget Management:** Compares the total rental cost with the customer's budget.
- **Alternative Car Suggestions:** Recommends other available models within the specified budget.
- **Final Bill Generation:** Displays customer details and the rental cost breakdown when the selected car fits the budget.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Data Structures:** Lists and dictionaries
- **Concepts:** Conditional statements, loops, indexing, membership operators, and formatted strings
- **Input/Output:** Console-based interaction

## 🚘 Available Car Brands

| Brand | Available Models |
|---|---|
| BMW | X1, X3, X5, Z4 Roadster |
| Tesla | Model X, Model Y, Model 3 |
| Mercedes | C-class, A-class, GLA SUV |

Rental prices and security deposits are defined within the Python program.

## 📂 Project Structure

```text
Swamiraj-Renters/
│
├── car_renter.py
└── README.md
```

## ⚙️ How It Works

1. The program welcomes the customer.
2. It collects the customer's name, age, and driving license status.
3. It verifies the customer's eligibility to rent a car.
4. The customer selects a car brand.
5. The program displays the models available under that brand, including rental prices and deposits.
6. The customer selects a model and enters the rental duration.
7. The program calculates the total rental cost.
8. The customer enters their budget.
9. If the selected car exceeds the budget, the program suggests other cars within the budget.
10. If the selected car fits the budget, the program generates the final bill.

## 💰 Rental Cost Calculation

The total rental cost is calculated using the following formula:

**Total Price = (Daily Rent × Number of Days) + Security Deposit**

For example, suppose a customer selects a BMW X1 with the following details:

| Description | Amount |
|---|---:|
| Daily rent | ₹3,000 |
| Rental duration | 2 days |
| Security deposit | ₹1,200 |
| **Total price** | **₹7,200** |

The example is illustrative and uses the prices defined in the program.

## ▶️ How to Run the Project

### Prerequisites

Install Python 3 on your computer.

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Folder

```bash
cd Swamiraj-Renters
```

### Step 3: Run the Program

```bash
python car_renter.py
```

If your system uses the `python3` command, run:

```bash
python3 car_renter.py
```

## 🧠 Concepts Demonstrated

- Python lists and dictionaries
- `if-elif-else` conditional statements
- `while` and `for` loops
- User input using `input()`
- Type conversion using `int()`
- Dictionary methods such as `.keys()`, `.values()`, and `.items()`
- List indexing and the `.index()` method
- Membership operators such as `in`
- String formatting using f-strings
- Basic financial calculations and budget comparisons

## 🚀 Future Enhancements

- Build a graphical user interface using Tkinter or Streamlit.
- Store vehicle information in a database such as MySQL or SQLite.
- Add customer login and booking history.
- Implement date-based reservations and vehicle availability tracking.
- Add input validation for invalid names, ages, rental durations, and budgets.
- Improve vehicle selection so customers can choose only models belonging to their selected brand.
- Generate downloadable invoices.
- Add payment integration and secure customer data management.

## ⚠️ Limitations

This is an educational, console-based project. It currently uses predefined vehicle data and does not maintain actual booking records, payment information, or real-time vehicle availability.

## 👨‍💻 Author

**Swamiraj Deshpande**

Computer Science and Engineering (AI & ML) Student

---

⭐ If you find this project useful, consider giving the repository a star!
