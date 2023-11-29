import os
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

environment_name = "CartPole-v1"
env = gym.make(environment_name)
# episodes = 5

# for episode in range(1, episodes + 1):
#     state = env.reset()
#     done = False
#     score = 0 

#     while not done:
#         env.render()
#         action = env.action_space.sample()
#         n_state, reward, truncate, done, info = env.step(action)
#         score += reward

#     print('Episode:{} Score:{}'.format(episode, score))
#     # env.close()  # Close the environment after each episode

# # Close the environment outside the loop
# env.close()

log_path = os.path.join('Reinforcement_Learning/Training', 'Logs')

print(log_path)

env = DummyVecEnv([lambda: gym.make(environment_name)])
model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=20000)
