#!/usr/bin/env python3

# https://docs.python.org/3.3/library/string.html#format-string-syntax

debug = False

class Bot:
    def __init__(self, color, test):
        self.color = color
        self.index = -1
        self.position = 1
        self.test = test
        self.get_next_move()

    def move(self, other_bot):
        if not self.has_move():
            return 'Stay at button {}'.format(self.position)
        if self.position != self.button:
            self.position += 1 if self.position < self.button else -1
            return 'Move to button {}'.format(self.position)
        if other_bot.has_move() and other_bot.index < self.index:
            # we have to wait for other bot
            return 'Stay at button {}'.format(self.position)
        # press our button
        self.button_pressed = True
        return 'Push button {}'.format(self.button)

    def end_of_move(self):
        if not self.has_move() or self.button_pressed:
            self.get_next_move()

    def get_next_move(self):
        self.button = 0
        self.button_pressed = False
        try:
            self.index = self.test.index(self.color, self.index + 1)
            self.button = int(self.test[self.index + 1])
            #print('next move for {} is to {}, index = {}'.format(self.color, self.button, self.index))
        except ValueError:
            #print('no next move for {}'.format(self.color))
            pass

    def has_move(self):
        return self.button != 0
    
def run_test(test):
    num_steps,*test = test.split()
    orange = Bot('O', test)
    blue = Bot('B', test)
    count = 0
    if debug:
        print('Time   | Orange             | Blue')
        print('-------+--------------------+-------------------')
    while True:
        if not orange.has_move() and not blue.has_move():
            break
        count += 1
        text1 = orange.move(blue)
        text2 = blue.move(orange)
        if debug:
            print('  {:^3}  | {:18} | {}'.format(count, text1, text2))
        orange.end_of_move()
        blue.end_of_move()
    return count
    
def do_test_cases(input_filename):
    with open(input_filename) as input:
        test_case_count = int(input.readline())
        for num, test in enumerate(input):
            print ('Case #{}: {}'.format(num + 1, run_test(test)))

if __name__ == '__main__':
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    do_test_cases(input_filename)
