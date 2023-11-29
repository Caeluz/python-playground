from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym
import numpy as np
import time

# Load the trained agent
model = PPO.load("Reinforcement_Learning/Training/Saved_Models/PPO_CartPole")

# Set the environment to the CartPole-v1
SEED = 42
env = gym.make('CartPole-v1', render_mode='human')
observation, info = env.reset(seed=SEED)

lastFailure = 0
for i in range(5000):
    # Replace random action selection with the model's prediction
    action, _ = model.predict(observation)
    
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        time.sleep(0.5)
        observation, info = env.reset()
        print(f'Environment reset after {i - lastFailure} steps')
        lastFailure = i

env.close()
    