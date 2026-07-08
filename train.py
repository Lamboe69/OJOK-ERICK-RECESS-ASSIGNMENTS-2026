from snake_game import SnakeGame
from agent import Agent
from agent import EPS_DECAY, EPS_END
import numpy as np

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0

    agent = Agent()
    game = SnakeGame(render=False)

    while True:
        state_old = game.get_state()
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)

        state_new = game.get_state()
        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print(f'Game {agent.n_games} | Score: {score} | Record: {record} | Epsilon: {agent.epsilon:.3f}')

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)

            agent.epsilon = max(EPS_END, agent.epsilon * EPS_DECAY)

if __name__ == '__main__':
    train()
