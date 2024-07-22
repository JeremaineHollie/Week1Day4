# Task 1

answer = True

while answer:
    user = input("Do you want to continue? ")
    if user == 'no':
        answer = False
        break

# Task 2

tacos = 1

while tacos <= 5:
    print("I am eating a taco!", tacos)
    tacos += 1
print("I am full!")