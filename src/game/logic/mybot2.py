import random,math
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
    


    def countDistance(self, a:Position,b:Position):
         return abs(b.x - a.x) + abs(b.y-a.y)
    
    def isCloseBase(self, a:Position,b:Position):
         if(self.countDistance(a,b) <= 8):
              return True
         

    def isEnoughDiamond(self,me : GameObject):
         if(me.properties.diamonds == 3):
              return True
         
    def getClosestTeleportPos(self,board:Board,me : GameObject):
        temp = []
        for i in range(len(board.game_objects)):
            if(board.game_objects[i].type == "TeleportGameObject"):
                 temp.append(board.game_objects[i].position)
                 

        if(self.countDistance(me.position,temp[0]) > self.countDistance(me.position,temp[1])):
             return temp[1]
        else:
             return temp[0]
    
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
            print(self.countDistance(me.position,temp[i].position) + "GameObj")
        

        return closestPos

    


              
              
              
        
        
             
                   
                   


    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties
        base = props.base
        current_position = board_bot.position
        list_go_diamond = []  # Create a local list to store DiamondGameObject instances

        for i in range(len(board.game_objects)):
            if(props.diamonds == 5):
                self.goal_position = base
                delta_x, delta_y = self.goTo(current_position,self.goal_position)
            else:
                if(self.isDiamondAvailable(board)):
                    if(self.isRedAvailable(board) and props.diamonds <=3):
                        self.goal_position = self.getRedPos(board)
                        delta_x, delta_y = self.goTo(current_position,self.goal_position)
                        print("red")
                    else:
                        if board.game_objects[i].type == "DiamondGameObject":
                            self.goal_position = board.game_objects[i].position
                            # list_go_diamond.append(board.game_objects[i])
                            delta_x, delta_y = self.goTo(current_position,self.goal_position)
                            print("blue")
                else:
                    if board.game_objects[i].type == "DiamondButtonGameObject":
                        self.goal_position = board.game_objects[i].position
                        delta_x, delta_y = self.goTo(current_position,self.goal_position)
                        
        
        # self.list_go = list_go_diamond

        # Your other logic...
        # delta_x, delta_y = get_direction(
        #     current_position.x,
        #     current_position.y,
        #     self.goal_position.x,
        #     self.goal_position.y,
        # )

        return delta_x, delta_y
