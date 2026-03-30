print("----------------- Welcome to Swamiraj Renters ------------------")

first, last = input("Enter your First and Last name: ").split()
age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ").lower()

print(f"\nWelcome {first},")

if age >= 18 and (license == 'yes' or license == 'y'):
    companies = ["BMW", "Tesla", "Mercedes"]
    bmw_models = {"X1":3000, "X3":5000, "X5":4500, "Z4 Roadster":5300}
    tesla_models = {"Model X":3500, "Model Y":3800, "Model 3":4000}
    mercedes_models = {"C-class":5000, "A-class":5500, "GLA SUV":4800}

    # Combined master lists
    model_list = list(bmw_models.keys()) + list(tesla_models.keys()) + list(mercedes_models.keys())
    rent_list = list(bmw_models.values()) + list(tesla_models.values()) + list(mercedes_models.values())
    deposit_list = [1200, 1000, 1100, 1300, 2000, 1800, 1900, 900, 950, 1000] 

    print("\n---------- Cars available at our showroom ----------")
    print("Rental Car Companies available")
    print("1. BMW")
    print("2. Tesla")
    print("3. Mercedes")

    while True:
        user_choice = int(input("\nEnter company number (1-3): "))
        if user_choice == 1:
            brand = "BMW"
            available_models = bmw_models 
        elif user_choice == 2:
            brand = "Tesla"
            available_models = tesla_models
        elif user_choice == 3:
            brand = "Mercedes"
            available_models = mercedes_models
        else:
            print("Invalid choice. Try again.")
            continue
        break

    print(f"\nAvailable models in {brand}:")
    for model, rent in available_models.items():
        full_index = model_list.index(model)
        deposit = deposit_list[full_index]
        print(f"Model: {model}  →  Rent per day: ₹{rent}  →  Deposit: ₹{deposit}")


    while True:
        model = input("Enter the model you want to rent: ")
        if model in model_list:
            index = model_list.index(model)
            rent = rent_list[index]
            deposit = deposit_list[index]
            break
        else:
            print("Model not available. Try again.")

    days = int(input("Enter number of days to rent the car: "))
    total_price = (rent * days) + deposit

    # Ask for budget
    user_budget = int(input("Enter your budget: ₹"))

    if total_price > user_budget:
        print("\nSorry, this car is out of your budget.")
        print("Here are other cars within your budget (excluding your chosen car):")
        
        for i in range(len(model_list)):
            if model_list[i] != model:
                alt_total = (rent_list[i] * days) + deposit_list[i]
                if alt_total <= user_budget:
                    print(f"→ {model_list[i]} | Rent: ₹{rent_list[i]}/day | Deposit: ₹{deposit_list[i]} | Total: ₹{alt_total}")
    else:
        print("\n----------------- Final Bill -----------------")
        print("Customer Name :", first, last)
        print("Age           :", age)
        print("License       :", license)
        print("Brand         :", brand)
        print("Model         :", model)
        print("Days          :", days)
        print("Rent per day  : ₹", rent)
        print("Deposit       : ₹", deposit)
        print("Total Price   : ₹", total_price)

else:
    print("\nSorry, you are not eligible to rent a car.")
