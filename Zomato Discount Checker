has_gold = input("Do you have Zomato Gold? (yes/no): ").lower()
bill = int(input("Enter your bill amount: "))

if has_gold == 'yes':
    if bill >= 199:
        discount = bill * 0.10
        final_bill = bill - discount
        print(f"Discount: ₹{discount}")
        print(f"Final bill: ₹{final_bill}")
        print("✓ Free delivery included")
    else:
        print(f"Bill amount: ₹{bill}")
        print("No discount (minimum ₹199 required)")
else:
    if bill >= 299:
        print(f"Bill amount: ₹{bill}")
        print("✓ Free delivery included")
    else:
        print(f"Bill amount: ₹{bill}")
        print("No discount or free delivery")
