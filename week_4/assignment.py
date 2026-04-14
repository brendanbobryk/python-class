income = float(input("Enter your annual income: $"))

if income < 15_750:
    taxable_income = 0
else:
    taxable_income = income - 15_750

if taxable_income >= 0 and taxable_income <= 11_925:
    print("Based on your taxable income, your tax rate is 10%")
elif taxable_income >= 11_926 and taxable_income <= 48_475:
    print("Based on your taxable income, your tax rate is 12%")
elif taxable_income >= 48_476 and taxable_income <= 103_350:
    print("Based on your taxable income, your tax rate is 22%")
elif taxable_income >= 103_351 and taxable_income <= 197_300:
    print("Based on your taxable income, your tax rate is 24%")
elif taxable_income >= 197_301 and taxable_income <= 250_525:
    print("Based on your taxable income, your tax rate is 32%")
elif taxable_income >= 250_526 and taxable_income <= 626_350:
    print("Based on your taxable income, your tax rate is 35%")
else:
    print("Based on your taxable income, your tax rate is 37%")