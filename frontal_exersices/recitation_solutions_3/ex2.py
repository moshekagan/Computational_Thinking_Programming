END_COMMAND = 'quit'

user_input = input("Insert a number or " + END_COMMAND + " to leave the program: ")

while user_input != END_COMMAND:
    print(int(user_input) ** 2)
    user_input = input("Insert a number or " + END_COMMAND + " to leave the program: ")

print("Bye Bye!")
