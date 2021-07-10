from collections import Counter

users = {"oyindamola":[],"kevin":[],"brianna":[],"patrice":[],"mario":[],"chris":[]}
body_mass_index = []

underweight = range(0,19)
normalweight = range(20,25)
overweight = range(26,30)
udw = []
nmw = []
ovw = []

def body_mass(height, weight):
    bmi = (weight/height**2) * 703
    return round(bmi,2)

def weight(b):
    if b in underweight:
        udw.append(b)
    elif b in normalweight:
        nmw.append(b)
    else:
        ovw.append(b)

for user, value in users.items():
    h = float(input("\n"+user.title()+", input your Height in inches: "))
    value.append(h)
    w = float(input("Input your Weight in pounds: "))
    value.append(w)

for user, value in users.items():
    bm = body_mass(value[0],value[1])
    body_mass_index.append(bm)

for mass in body_mass_index:
    weight(mass)

print(body_mass_index)