secret_number = 2022
guess_count = 0
guess_limit = 4 

print("Welcome to danilo's phone")
while guess_count < guess_limit:
    guess = int(input("Enter your pin bana: "))
    guess_count += 1

    if guess == secret_number:
        print("Welcome, you are logged in!")
        break

else:
    print("Ooooops, bana huezi ingia huku!!")