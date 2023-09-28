# Ternary operator
a = 5

if a > 0:
    checker = "Positive"
else:
    checker = "Negative"

checker = "Positive" if a > 0 else "Negative"

truthy = True
cat = ("angry", "nice")[truthy]  # - значення в квадратних дужках це SLISE
print(f"Cat is {cat}")
# Cat is nice
# because (index[0]="angry") 0 is False
