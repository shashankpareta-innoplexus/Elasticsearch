

a = ["shashank", "Pradumna", "pareta", "hitesh", "mahesh"]
b = [{"age" : 23 }]

new = []

for i in range(len(a)):
    new.append({"name" : a[i], "gender": "male"})

b.append({"all_names" : new})

print b
