import gymnasium as gym
from stable_baselines3 import A2C
# Many environment at the same time
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_atari_env
import os

#http://atarimania.com/roms/Roms.rar
# python -m atari_py.import_roms <path-to-roms>

environment_name = "Breakout-v4"
env = gym.make(environment_name, render_mode='human', frameskip=4)
# env = gym.make(environment_name, frameskip=4)
path = 'Reinforcement_Learning'

# Set render fps if it's not defined
if 'render_fps' not in env.metadata:
    env.metadata['render_fps'] = 30  

def model_random_test():
    episodes = 5
    for episode in range(1, episodes+1):
        state, info = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            n_state, reward, truncate, done, info = env.step(action)
            score += reward
        print('Episode:{} Score:{}'.format(episode, score))
    env.close()


def vec_env_and_model_train():
    # Create the environment
    env = make_atari_env(environment_name, n_envs=4, seed=0)
    # Stack 4 frames
    env = VecFrameStack(env, n_stack=4)
    
    # Create logs
    log_path = os.path.join(path, 'Training', 'Logs',)

    # Create the agent
    model = A2C('CnnPolicy', env, verbose=1, tensorboard_log=log_path)
    # Train the agent
    model.learn(total_timesteps=1000)

    # Save the agent
    a2c_path = os.path.join(path, 'Training', 'Saved_Models', 'a2c_Breakout_Model_1_env')
    model.save(a2c_path)

    # Evaluate the agent
    mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

    print(f"mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")

    # Enjoy trained agent
    # obs = env.reset()
    # for i in range(1000):
    #     action, _states = model.predict(obs)
    #     obs, rewards, dones, info = env.step(action)
    #     env.render()


def test_model():
    # Load the trained agent
    env = make_atari_env('Breakout-v4', n_envs=1, seed=0)
    env= VecFrameStack(env, n_stack=4)
    # print(make_atari_env)
    model = A2C.load("Reinforcement_Learning/Training/Saved_Models/A2C_model", env=env, verbose=1)

    # # Evaluate the agent
    # mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

    # print(f"mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")

    # Trained
    episodes = 5
    for episode in range(1, episodes+1):
        obs = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            # Instead of randomly selecting an action, the model predicts the next action
            action, _ = model.predict(obs)
            obs, reward, truncate, done, info = env.step(action)
            score += reward

        print('Episode:{} Score:{}'.format(episode, score))


def test_model_2():
    env = make_atari_env('Breakout-v4', n_envs=1, seed=0)
    env = VecFrameStack(env, n_stack=4)
    model = A2C.load("Reinforcement_Learning/Training/Saved_Models/A2C_model", env, verbose=1)
    evaluate_policy(model, env, n_eval_episodes=10, render=True)


def test_model_3():
    env = gym.make('Breakout-v4')
    model = A2C.load("Reinforcement_Learning/Training/Saved_Models/a2c_Breakout_Model_1_env", env, verbose=1)
    mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
    
    print(f"mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")
    
    # Trained
    obs = env.reset()
    for i in range(1000):
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render()


def test_model_4():
    # Create the Breakout environment with the desired observation space
    env = make_atari_env('Breakout-v4', n_envs=1, seed=0)
    env = VecFrameStack(env, n_stack=4)

    # Load the trained A2C model
    model = A2C.load("Reinforcement_Learning/Training/Saved_Models/a2c_Breakout_Model_1_env", env=env, verbose=1)

    # Evaluate the policy
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10, render=True)
    print(f"mean_reward: {mean_reward:.2f} +/- {std_reward:.2f}")

    # Test the model on one environment
    # obs = env.reset()
    # for i in range(1000):
    #     action, _ = model.predict(obs)
    #     obs, rewards, dones, info = env.step(action)
    #     env.render()

    env.close()
    
    
def main():
    # model_random_test()
    # vec_env_and_model_train()
    # test_model()
    # test_model_2()
    # test_model_3()
    test_model_4()
    
    

if __name__ == '__main__':
    main()
