import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


'''
point diamond merah = 2
Gameobject :  DiamondGameObject,BotGameObject,DiamondButtonGameObject,TeleportGameObject 



'''

class MyBot(BaseLogic):
    
            

            



    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0
        # self.list_go: Optional[List[GameObject]] = []   Initialize as an empty list


    def isDiamondAvailable(self,board: Board):
            diamond = 0
            for i in range(len(board.game_objects)):
                if board.game_objects[i].type == "DiamondGameObject":
                    diamond += 1

            return diamond > 0

    def isRedAvailable(self,board: Board):
            red = 0
            for i in range(len(board.game_objects)):
                if board.game_objects[i].type == "DiamondGameObject" and board.game_objects[i].properties.points == 2:
                    red += 1

            return red > 0

    def getRedPos(self,board:Board):
        for i in range(len(board.game_objects)):
                if board.game_objects[i].type == "DiamondGameObject" and board.game_objects[i].properties.points == 2:
                    return board.game_objects[i].position

    def goTo(self,a : Position,b:Position):
        delta_x,delta_y = get_direction(a.x,a.y,b.x,b.y)
        return delta_x,delta_y



    def next_move(self, board_bot: GameObject, board: Board):
        delta_x = 0
        delta_y = 1
        return delta_x, delta_y
