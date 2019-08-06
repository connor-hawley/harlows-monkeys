import numpy as np
from k_armed_bandit_independent_bernoulli import kArmedBanditIndepentBernoulli as Bandit
from agent_random import RandomAgent
import matplotlib.pyplot as plt

# runs experiment one - bandits with independent arms

# setup
num_episodes = 100
len_episode = 100
num_arms = 2
ps = np.random.sample(num_arms)

exp1_bandit = Bandit(num_arms, ps)
random_agent = RandomAgent(num_arms)

cum_reward = np.zeros((num_episodes, 1))
for i in range(num_episodes):
    current_cum_rewards = 0
    for j in range(len_episode):
        cur_action = random_agent.get_policy()
        current_cum_rewards += exp1_bandit.pull_arm(cur_action)
    cum_reward[i] = current_cum_rewards

plt.plot(cum_reward)
plt.show()
