import math_calc


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print({
    "sum": math_calc.add(a, b),
    "difference": math_calc.subtract(a, b),
    "product": math_calc.multiply(a, b),
    "quotient": math_calc.divide(a, b),
    "power":  math_calc.power(a, b)
})
