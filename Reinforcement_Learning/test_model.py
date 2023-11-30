from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold
from stable_baselines3.common.evaluation import evaluate_policy
import gymnasium as gym
import numpy as np
import time

# Load the trained agent
model = PPO.load("Reinforcement_Learning/Training/Saved_Models/PPO_CartPole",)

# Set the environment to the CartPole-v1
SEED = 42
env = gym.make('CartPole-v1', render_mode='human')
# env = gym.make('CartPole-v1')
observation, info = env.reset(seed=SEED)
lastFailure = 0


def run_model():
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
    
    
def evaluate_model():
    evaluate_policy(model, env, n_eval_episodes=10, render=True)


def test_model():
    episodes = 5
    for episode in range(1, episodes + 1):
        obs, info = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            # Instead of randomly selecting an action, the model predicts the next action
            action, _ = model.predict(obs)
            obs, reward, truncate, done, info = env.step(action)
            score += reward

        print('Episode:{} Score:{}'.format(episode, score))
    env.close()  # Close the environment after each episode


# View Logs
# tensorboard --logdir=Training/Logs/PPO_2/

def model_callback():
    stop_callback = StopTrainingOnRewardThreshold(reward_threshold=200, verbose=1)
    eval_callback = EvalCallback(env, callback_on_new_best=stop_callback, eval_freq=10000, best_model_save_path='Training/Saved_Models/', verbose=1)
    
    model = PPO('MlpPolicy', env, verbose=1, tensorboard_log='Reinforcement_Learning/Training/Logs/')
    model.learn(total_timesteps=20000, callback=eval_callback)
    
    return stop_callback, eval_callback, model


def change_policy():
    net_arch = [dict(pi=[128, 128, 128, 128], vf=[128, 128, 128, 128])]
    model = PPO('MlpPolicy', env, verbose=1, tensorboard_log='Reinforcement_Learning/Training/Logs/', policy_kwargs={'net_arch': net_arch})    
    eval_callback = model_callback()
    
    model.learn(total_timesteps=20000, callback=eval_callback)


def main():
    # run_model()
    # evaluate_model()
    test_model()
    # model_callback()
    # change_policy()


if __name__ == "__main__":
    main()