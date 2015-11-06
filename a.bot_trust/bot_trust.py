#!/usr/bin/env python3

class Bot:
    def __init__(self, color, test):
        self.color = color
        self.index = -1
        self.position = 1
        self.test = test
        self.get_next_move()

    def move(self, other_bot):
        if not self.has_move():
            return
        if self.position != self.button:
            last = self.position
            self.position += 1 if self.position < self.button else -1
            #print('{}: move from {} to {}'.format(self.color, last, self.position))
            return
        if other_bot.has_move() and other_bot.index < self.index:
            # we have to wait for other bot
            #print('{}: waiting for {} to press their button'.format(self.color, other_bot.color))
            return
        # press our button
        #print('{}: pressing button {}'.format(self.color, self.button))
        self.button_pressed = True

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
    #print(int(num_steps))
    orange = Bot('O', test)
    blue = Bot('B', test)
    count = 0
    while True:
        if not orange.has_move() and not blue.has_move():
            break
        count += 1
        #print('-----'*3,count,'-----'*3)
        orange.move(blue)
        blue.move(orange)
        orange.end_of_move()
        blue.end_of_move()
    return count
    
def do_test_cases(input_filename):
    with open(input_filename) as input:
        test_case_count = int(input.readline())
        #print(test_case_count)
        for num, test in enumerate(input):
            #print(test.strip())
            print ('Case #{}: {}'.format(num + 1, run_test(test)))

if __name__ == '__main__':
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    do_test_cases(input_filename)
