# print each donut 
# print("you have eaten 1 donuts.")
# print("you have eaten 2 donuts.")
# print("you have eaten 3 donuts.")
# print("you have eaten 4 donuts.")
# print("you have eaten 5 donuts.")
# print("you have eaten 6 donuts.")
# print("you have eaten 7 donuts.")
# print("you have eaten 8 donuts.")
# print("you have eaten 9 donuts.")
# print("you have eaten 10 donuts.")

donuts_eaten = 1
while donuts_eaten <= 10:
    print(f"you have eaten {donuts_eaten} donuts.")
    # donuts_eaten = donuts_eaten + 1
    # without something that gets us closer to breaking the loop
    # we end up with an infinite loop
    donuts_eaten += 1

# Infinite loops can be good
while True:
    print("working...")
    user_input = input("Should I stop? (y/n) ")
    if user_input == 'y':
        print("thank you!")
        # stop a loop with break keyword
        break
    else:
        print("sigh...")

donuts_to_eat = int(input("How many donuts will you eat? "))
user_donuts_eaten = 0
while user__donuts_eaten <= donuts_to_eat:
    user_donuts_eaten += 1
    print(f"you have eaten {user_donuts_eaten} donuts.")
        if (user_donuts_eaten == donuts_to_eat / 2):
            print("you're halfway there")