import numpy.random as rd


class kArmedBanditNormal:
    def __init__(self, num_arms, means, stds):
        self.num_arms = num_arms
        self.means = means
        self.stds = stds

    def __repr__(self):
        return '{}-armed bandit with means {} and stds {}'.format(self.num_arms, self.means, self.stds)

    def __str__(self):
        out = '{} arms: '.format(self.num_arms)
        for i in range(self.num_arms):
            out += '({}, {}), '.format(self.means[i], self.std[i])
        return out[:-2]

    def pull_arm(self, arm_no):
        return rd.normal(self.means[arm_no], self.stds[arm_no])

    def add_arm(self, mean, std):
        self.num_arms += 1
        self.means.append(mean)
        self.stds.append(std)
