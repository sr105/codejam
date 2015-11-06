#!/usr/bin/env python3

"""
Solution for Problem A. Bot Trust

https://code.google.com/codejam/contest/975485/dashboard
"""

DEBUG = 0

class Bot(object):
    """Bot that moves and presses buttons"""
    def __init__(self, color, test):
        self.color = color
        self.index = -1
        self.position = 1
        self.test = test
        self.button = 0
        self.button_pressed = False
        self.get_next_move()

    def move(self, other_bot):
        """makes a move or presses a button if possible"""
        if not self.has_move():
            return 'Stay at button {}'.format(self.position)
        if self.position != self.button:
            self.position += 1 if self.position < self.button else -1
            return 'Move to button {}'.format(self.position)
        if other_bot.has_move() and other_bot.index < self.index:
            # we have to wait for the other bot
            return 'Stay at button {}'.format(self.position)
        # press our button
        self.button_pressed = True
        return 'Push button {}'.format(self.button)

    def end_of_move(self):
        """perform end of move operations once all bots have moved"""
        if not self.has_move() or self.button_pressed:
            self.get_next_move()

    def get_next_move(self):
        """get the next available move for this bot"""
        self.button = 0
        self.button_pressed = False
        try:
            self.index = self.test.index(self.color, self.index + 1)
            self.button = int(self.test[self.index + 1])
            if DEBUG > 1:
                print('{}: next move is to {}, index = {}'.format(self.color,
                                                                  self.button,
                                                                  self.index))
        except ValueError:
            if DEBUG > 1:
                print('{}: no next move'.format(self.color))

    def has_move(self):
        """reports whether or not this bot has any moves remaining"""
        return self.button


def run_test(test):
    """run a single test case"""
    test = test.split()[1:]
    orange = Bot('O', test)
    blue = Bot('B', test)
    count = 0
    if DEBUG:
        print('Time   | Orange             | Blue')
        print('-------+--------------------+-------------------')
    while True:
        if not orange.has_move() and not blue.has_move():
            break
        count += 1
        text1 = orange.move(blue)
        text2 = blue.move(orange)
        if DEBUG:
            print('  {:^3}  | {:18} | {}'.format(count, text1, text2))
        orange.end_of_move()
        blue.end_of_move()
    return count

def do_test_cases(filename):
    """read test case lines from filename and process them"""
    with open(filename) as test_cases:
        test_cases.readline() # test_case_count
        for num, test in enumerate(test_cases):
            print ('Case #{}: {}'.format(num + 1, run_test(test)))

if __name__ == '__main__':
    import sys
    if not DEBUG and len(sys.argv) == 1:
        DEBUG = 1
    do_test_cases(sys.argv[1] if len(sys.argv) > 1 else 'first_input.txt')
