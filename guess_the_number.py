from random import randint
lower_num,upper_num=1,10
random_num: int=randint(lower_num,upper_num)
print(f"Guess the number in the range from {lower_num} to {upper_num} .")
a=0
while a<3:
    try:
        user_guess: int=int(input("Guess: "))
    except ValueError :
        print("Please enter a valid number.")
        continue
    a+=1
    if a==3:
        print("Game over.")
        break
    elif user_guess>random_num:
        print("The number is lower")

    elif user_guess<random_num:
        print("The number is higher.")

    else:
        print("You guessed it!")
        break
