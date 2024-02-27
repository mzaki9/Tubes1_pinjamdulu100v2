from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


'''
Gameobject : DiamondGameObject,BotGameObject,DiamondButtonGameObject,TeleportGameObject,BaseGameObject
Board : Board
'''

class ChadBot(BaseLogic):
    def __init__(self):
        self.current_direction = 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def next_move (self,board_bot: GameObject, board: Board):
        props.bot = board_bot.properties
        



        