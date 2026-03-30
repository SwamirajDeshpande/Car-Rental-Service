# 🚗 Car Rental Service
## 📌 Overview

Car Rental Service is a simple Python-based console application that allows users to rent cars from different companies like BMW, Tesla, and Mercedes. The system checks user eligibility, displays available cars, calculates rental cost, and suggests alternatives based on budget.

## ✨ Features
✅ User eligibility check (Age & Driving License)

🚘 Multiple car brands:
BMW
Tesla
Mercedes

📋 Displays available models with:
Rent per day
Security deposit

💰 Budget-based filtering

🔄 Suggests alternative cars within budget

🧾 Generates final bill

## 🛠️ Technologies Used
Python (Core Python)
Console-based input/output

## 📂 Project Structure
car_renter.py   # Main application file

README.md       # Project documentation

## ▶️ How to Run
Make sure Python is installed (Python 3.x recommended)

Download or clone the project

Run the file:
python car_renter.py

## 🧑‍💻 How It Works
User enters:
Name
Age
Driving license status
System checks eligibility:
Must be 18+
Must have a valid license
User selects:
Car company
Model
Number of days

System calculates:

Total Price = (Rent × Days) + Deposit
Budget Check:
If within budget → Show bill
If not → Suggest alternatives

## 📊 Sample Output
Welcome Swamiraj,

Available models in BMW:
Model: X1 → Rent per day: ₹3000 → Deposit: ₹1200

Enter model: X1
Enter days: 2
Enter budget: ₹7000

Final Bill:
Total Price: ₹7200
## 🚀 Future Improvements
GUI using Tkinter

Database integration

Online booking system

Payment gateway integration

Admin dashboard
## 👨‍💻 Author

Swamiraj Deshpande

## 📜 License

This project is for educational purposes.
