import random


class Dice:

    def __init__(self):
        self.faces_ui = {
            1: '''
         _________
        |         |
        |         |
        |    0    |
        |         |
        |_________|
        ''', 2: '''
         _________
        |         |
        |         |
        |  0   0  |
        |         |
        |_________|
        ''', 3: '''
         _________
        |         |
        |         |
        | 0  0  0 |
        |         |
        |_________|
        ''', 4: '''
        ┌─────────┐
        |         |
        |  0   0  |
        |         |
        |  0   0  |
        └─────────┘
        ''', 5: '''
         _________
        |         |
        |  0   0  |
        |    0    |
        |  0   0  |
        |_________|
        ''', 6: '''
         _________
        |         |
        | 0  0  0 |
        |         |
        | 0  0  0 |
        |_________|
        ''', }

    def roll(self, print_result=False):
        faces = [1, 2, 3, 4, 5, 6]
        result = random.choice(faces)

        if print_result:
            print(self.faces_ui[result])

        return result
