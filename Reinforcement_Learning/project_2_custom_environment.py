# Import gym and other necessary Python packages
import gymnasium as gym
from gymnasium import Env
from gymnasium.spaces import Discrete, Box, Tuple, Dict, MultiBinary, MultiDiscrete

# Import helper functions
import numpy as np
import random
import os

# Import stable_baselines
from stable_baselines3 import PPO, DQN, A2C, SAC
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

# Gym Spaces
# four key types of spaces: Discrete, Box, MultiBinary, MultiDiscrete
# two wrapper spaces: Tuple and Dict (two help group different spaces together)


# Bulding a custom environment
# Buld an agent, random temperature, 37 and 39 degrees

class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up for the temperature
        self.action_space = Discrete(3)
        self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        self.state = 38 + random.randint(-3,3)
        self.shower_length = 60
        
    def step(self, action):
        # Apply action or temperature change
        self.state += action-1 
        
        # Decrease shower time
        self.shower_length -= 1
        
        # Calculate reward
        if self.state >= 37 and self.state <=39:
            reward = 1
        else:
            reward = -1        
            
        # Check if shower is done
        if self.shower_length <= 0:
            done = True
        else:
            done = False
        
        info = {}
        
        return self.state, reward, done, info
        
    def render(self):
        # Implement viz
        pass
    def reset(self):
        self.state = np.array([38+random.randint(-3,3)]).astype(float)
        self.shower_length = 60
        return self.state

# Create the environment
env = ShowerEnv()

# test the environment
# episodes = 5
# for episode in range(1, episodes+1):
#     state = env.reset()
#     done = False
#     score = 0 
    
#     while not done:
#         env.render()
#         action = env.action_space.sample()
#         n_state, reward, done, info = env.step(action)
#         score += reward
#     print('Episode:{} Score:{}'.format(episode, score))
# env.close()

# Train Model
path = 'Reinforcement_Learning'
log_path = os.path.join(path, 'Training', 'Logs')
model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=4000)

# Save Model
shower_path = os.path.join(path, 'Training', 'Saved Models', 'PPO_shower')
model.save(shower_path)