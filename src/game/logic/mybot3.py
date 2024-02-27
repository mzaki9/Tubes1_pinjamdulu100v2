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
        usPos = board_bot.position
        goal = board_bot.properties.base
        if (board_bot.properties.diamonds == 5):
            
            delta_x , delta_y = self.goTo(usPos,goal)
        else:

            tempPost = self.getClosestDiamondPos(board,board_bot)
            delta_x , delta_y = self.goTo(usPos,tempPost)


        return delta_x, delta_y

    def countDistance(self, a:Position,b:Position):
         return abs(b.x - a.x) + abs(b.y-a.y)

    def getClosestDiamondPos(self,board:Board, me : GameObject):
        temp = []
        for i in range(len(board.game_objects)):
            if(board.game_objects[i].type == "DiamondGameObject"):
                temp.append(board.game_objects[i])

        closestPos : GameObject.position
        closestDist = 99999

        for i in range(len(temp)):
            if(self.countDistance(me.position,temp[i].position) < closestDist):
                closestDist = self.countDistance(me.position,temp[i].position)
                closestPos = temp[i].position
        

        return closestPos
