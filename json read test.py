import json

# f= open('user.key', 'r')
# print(f.read())

with open('user.key', 'r') as f:
    user_dict = json.load(f)
    print(user_dict)
    print(user_dict['Username'])
    print(user_dict['Password'])
    f.close()