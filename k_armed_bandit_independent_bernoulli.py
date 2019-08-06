import numpy.random as rd


class kArmedBanditIndepentBernoulli:
    def __init__(self, num_arms, ps):
        self.num_arms = num_arms
        self.ps = ps

    def __repr__(self):
        return '{}-armed bandit with bernoulli probabilities {}'.format(self.num_arms, self.ps)

    def __str__(self):
        out = '{} arms: '.format(self.num_arms)
        for i in range(self.num_arms):
            out += '{}, '.format(self.ps[i])
        return out[:-2]

    def pull_arm(self, arm_no):
        return rd.binomial(1, self.ps[arm_no])

    def add_arm(self, p):
        self.num_arms += 1
        self.ps.append(p)