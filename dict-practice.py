menu = {"popcorn":150,"soda":90,"nachos":120}
soda_price = menu["soda"]
nachos_price = menu["nachos"]
total_bill = soda_price + nachos_price
print(f'total bill:{total_bill}')
#output: total_bill: 210
students_atten = {"Rahul":"present","Sneha":"present","Vikram":"absent"}
print(students_atten.get("present"))
print(students_atten.values())
print(students_atten.keys())
print(students_atten.items())
