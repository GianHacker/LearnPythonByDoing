# while loop in python

is_learning = True

while is_learning:
    print("You are learning!")
    user_input = input("Are you still learning: ")
    is_learning = user_input == 'yes'

# for loop in python

friends = ['Rolf','Bob','Anne']

for friend in friends:
    print(friend)