# import section
import random

# function section
def guess_the_number():
    lower_bound = 1
    upper_bound = 100
    guessed_number = random.randint(lower_bound, upper_bound)
    max_attempts = 7

    # welcome section
    print(f"Вітаю! Я загадав число від {lower_bound} до {upper_bound}. Спробуй вгадати його за {max_attempts} спроб.")

    # cycle section
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Введіть ваше припущення: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        # condition section
        if guess < guessed_number:
            print("Занадто маленьке!")
        elif guess > guessed_number:
            print("Занадто велике!")
        else:
            print(f"Ви вгадали! Це число {guessed_number}.")
            break
    else:
        print(f"На жаль, ви не вгадали. Загадане число було: {guessed_number}")

# function call
if __name__ == "__main__":
    guess_the_number()
