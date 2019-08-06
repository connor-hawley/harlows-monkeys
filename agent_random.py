import numpy.random as rd


class RandomAgent:
    def __init__(self, num_actions):
        self.num_actions = num_actions

    def get_policy(self):
        return rd.randint(0, self.num_actions)