# Ask for name
user_name = input("What is your name? ")
# greet user
print(f"Hello, {user_name}")

# the code on line 7 and 8 will print True or False
# name_is_long = len(user_name) > 10
# print(name_is_long)

# check if name is longer than 10
if len(user_name) > 10:
    # if it is say 'wow, long name'
    print('match 10')
elif len(user_name) > 5:
    print('match 5')
else:
    print('match everything else')
    # if name is not longer than 10
# if len(user_name) < 10:
    # print 'short name'
# else:
#     print('cool name')

print('done')
