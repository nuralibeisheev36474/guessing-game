import random


class Number:
    def __init__(self):
        self.value = random.randint(1, 99)


class Result:
    def check(self, guess, number):
        if guess == number.value:
            return "win"
        elif guess > number.value:
            return "high"
        else:
            return "low"


class Game:
    def __init__(self):
        self.number = Number()
        self.attempts = 5
        self.score = 0

    def play(self):
        print("Game started!")

        while self.attempts > 0:
            guess = int(input("Guess the number: "))

            result = Result().check(guess, self.number)

            if result == "win":
                print("You won!")
                self.score += 1
                return
            elif result == "high":
                print("Too high")
            else:
                print("Too low")

            self.attempts -= 1

        print("You lost!")
        print("Score:", self.score)


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()