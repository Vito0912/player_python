import logging
import os
import sys

# Get the current file's directory
current_dir = os.path.dirname(__file__)

# Construct the path to the 'socha' module
socha_path = os.path.join(current_dir, 'python', 'socha')

# Add the 'socha' module to the system path
sys.path.append(socha_path)

from socha import (
    GameState,
    Move,
    Advance
)
from socha.api.networking.game_client import IClientHandler
from socha.starter import Starter


class Logic(IClientHandler):
    game_state: GameState

    # this method is called every time the server is requesting a new move
    # this method should always be implemented otherwise the client will be disqualified
    def calculate_move(self) -> Move:
        return Move(action=Advance(distance=1, cards=[]))

    # this method is called every time the server has sent a new game state update
    # this method should be implemented to keep the game state up to date
    def on_update(self, state: GameState) -> None:
        self.game_state = state


if __name__ == "__main__":
    Starter(logic=Logic())
    # if u wanna have more insights, u can set the logging level to debug:
    # Starter(logic=Logic(), log_level=logging.DEBUG)
