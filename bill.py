units = float(input("Enter units consumed: "))
rate_per_unit = 5.0
total_bill = units * rate_per_unit

discount = 0
if total_bill > 1000:
    discount = total_bill * 0.10

final_bill = total_bill - discount

print(f"Units Consumed: {int(units) if units.is_integer() else units}")
print(f"Total Bill: ₹{int(total_bill) if total_bill.is_integer() else total_bill}")
print(f"Discount Applied: ₹{int(discount) if discount.is_integer() else discount}")
print(f"Final Bill: ₹{int(final_bill) if final_bill.is_integer() else final_bill}")
