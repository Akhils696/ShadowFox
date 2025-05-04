def set_expenses(person):
    print(f"\nEnter {person}'s expenses:")
    expenses={}
    expenses["Hotel"]=float(input("Hotel: ₹"))
    expenses["Food"]=float(input("Food: ₹"))
    expenses["Transportation"]=float(input("Transportation: ₹"))
    expenses["Attractions"]=float(input("Attractions: ₹"))
    expenses["Miscellaneous"]=float(input("Miscellaneous: ₹"))
    return expenses

def compare_expenses(your_expenses, partner_expenses):
    your_total=sum(your_expenses.values())
    partner_total=sum(partner_expenses.values())
    print(f"\nYour total expenses: ₹{your_total}")
    print(f"Partner's total expenses: ₹{partner_total}")

    if your_total>partner_total:
        print("You spent more overall.")
    elif partner_total>your_total:
        print("Your partner spent more overall.")
    else:
        print("Both of you spent the same amount.")
    max_diff=0
    diff_category=""
    print("\nCategory-wise differences:")
    for category in your_expenses:
        diff=abs(your_expenses[category]-partner_expenses[category])
        print(f"{category}: ₹{diff}")
        if diff>max_diff:
            max_diff=diff
            diff_category=category

    print(f"\nThe category with the biggest spending difference is '{diff_category}' with a difference of ₹{max_diff}.")

your_expenses=set_expenses("your")
partner_expenses=set_expenses("partner")
compare_expenses(your_expenses, partner_expenses)
