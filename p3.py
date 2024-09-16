bill_amount = float(input("Enter the bill amount ($): "))
tip_percentage = float(input("Enter tip percentage (%): "))

tip_amount = bill_amount * (tip_percentage/100)
final_amount = bill_amount + tip_amount

print(f"A {tip_percentage}% tip on ${bill_amount} equals ${tip_amount} ")
print(f"The total bill is: ${final_amount}")