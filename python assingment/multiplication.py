number = int(input("enter a number to genrate its multiplication table:"))
multiplier =1
print(f"multiplication table for {number}:")
while multiplier <=10:
    result = number*multiplier
    print(f"{number}*{multiplier}={result}")
    multiplier +=1
    