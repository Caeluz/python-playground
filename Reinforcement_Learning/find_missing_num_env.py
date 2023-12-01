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


class FindMissingNumbers(gym.Env):
    def __init__(self):
        super(FindMissingNumbers, self).__init__()

        # Define the action and observation spaces
        self.action_space = Discrete(10)  # Actions are integer guesses from 0 to 9
        self.observation_space = Box(low=0, high=9, shape=(10,))

        # Set the maximum number of steps
        self.max_steps = 3

        # Initialize the environment with a random array and correct answer
        self.reset()

    def reset(self):
        # Generate a random array with missing numbers
        self.array = np.random.choice(10, size=6, replace=False)

        # Generate a pool of numbers not in self.array
        pool = np.setdiff1d(np.arange(10), self.array, assume_unique=True)

        # Randomly choose correct answer (missing numbers) from the pool
        self.correct_answer = np.random.choice(pool, size=3, replace=False)

        # Initialize the current guess
        self.current_guess = np.zeros(10)
        self.current_guess[self.array] = 1  # Set the initial state to include the numbers in the array

        # Reset the step counter
        self.current_step = 0

        return self.current_guess

    def step(self, action):
        # Update the current guess based on the agent's action
        self.current_guess[action] = 1

        # Calculate the reward
        reward = self._calculate_reward()

        # Check if the episode is done
        done = self.current_step == self.max_steps

        # Increment the step counter
        self.current_step += 1
        
        print(self.current_guess, self.correct_answer, reward, done)

        # Return the observation, reward, done flag, and additional info
        return self.current_guess, reward, done, {}

    def _calculate_reward(self):
        # Calculate the reward based on the correctness of the guess
        correctness = np.all(self.current_guess[self.array] == 1)  # Check if guessed positions are in array
        return 1.0 if correctness else 0.0

    def render(self, mode='human'):
        # Optionally, implement a rendering method for visualization
        pass

# env = FindMissingNumEnv()
env = FindMissingNumbers()
print(env.observation_space.sample())

# test the environment
episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0 
    
    while not done:
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode, score))
env.close()

path = 'Reinforcement_Learning'
log_path = os.path.join(path, 'Training', 'Logs')
model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=4000)

# Save Model
missing_num_path = os.path.join(path, 'Training', 'Saved Models', 'missing_num_ppo')
model.save(missing_num_path)