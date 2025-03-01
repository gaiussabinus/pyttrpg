import random

def dice(sides, number = 1, threshold = 0, mod = 0):
      dice_rolled = []
      total = 0
      while 0 < number:
          die = random.randint(1,sides)
          if die >= threshold:
            dice_rolled.append(die)
          number -= 1
      dice_rolled.sort()
      total = sum(dice_rolled) + mod
      return (*dice_rolled," + " + str(mod) + " = " + str(total))

def input_handler(string):
    sides = ""
    number_of_dice = ""
    threshold = 0
    mod = "0"
    is_number = True
    threshold_toggle = False
    mod_toggle = False

    for char in string:
        if char.isnumeric() and is_number:
          number_of_dice += char
        if char.lower() == "d":
          is_number = False
        if char.isnumeric() and not is_number and not threshold_toggle and not mod_toggle:
            sides += char
        if char.lower() == "t" and not is_number:
            threshold_toggle = True
        if char == "+" and not is_number:
            mod_toggle = True
        if char.isnumeric() and mod_toggle:
            mod += char
        if char.isnumeric() and not is_number and threshold_toggle:
            threshold = int(char)

    sides = int(sides)
    number_of_dice = int(number_of_dice)
    return sides, number_of_dice, threshold, int(mod)

if __name__ == "__main__":
    running = True
    print("Welcome to DiceRoller\npress q to quit\n Input in the format, d6 , 3d6, 3d6+5, or 3d6t3\n t stands for threshold for discarding dice\nPlease roll your dice\n")
    while running:
        user_input = input("|>")
        if user_input.lower() == "q":
            running = False
        else:
            user_input = input_handler(user_input)
            print(dice(sides = user_input[0], number = user_input[1], threshold = user_input[2], mod = user_input[3]))
    print("goodbye")
    exit()
