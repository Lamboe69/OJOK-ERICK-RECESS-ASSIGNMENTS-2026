from snake_game import SnakeGame
from agent import Agent

def play():
    agent = Agent()
    agent.model.load()
    agent.epsilon = 0

    game = SnakeGame(render=True)

    while True:
        state_old = game.get_state()
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)

        if done:
            print(f'Final Score: {score}')
            game.reset()

if __name__ == '__main__':
    play()
