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
                if board.game_objects[i].type == "DiamondGameObject" and board.game_objects[i].properties.points == 1:
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

    def getClosestDiamondPos(self,board:Board, me : GameObject):
        temp = []
        for i in range(len(board.game_objects)):
            if(board.game_objects[i].type == "DiamondGameObject" and board.game_objects[i].properties.points == 1):
                temp.append(board.game_objects[i])

        closestPos : GameObject.position
        closestDist = 99999

        for i in range(len(temp)):
            if(self.countDistance(me.position,temp[i].position) < closestDist):
                closestDist = self.countDistance(me.position,temp[i].position)
                closestPos = temp[i].position
        

        return closestPos
    def getClosestRedPos(self,board:Board, me : GameObject):
        temp = []
        for i in range(len(board.game_objects)):
            if(board.game_objects[i].type == "DiamondGameObject" and board.game_objects[i].properties.points == 2):
                temp.append(board.game_objects[i])

        closestPos : GameObject.position
        closestDist = 99999

        for i in range(len(temp)):
            if(self.countDistance(me.position,temp[i].position) < closestDist):
                closestDist = self.countDistance(me.position,temp[i].position)
                closestPos = temp[i].position
        

        return closestPos
    
    
    def getClosestTeleportPos(self,board:Board,me : GameObject):
        temp = []
        for i in range(len(board.game_objects)):
            if(board.game_objects[i].type == "TeleportGameObject"):
                 temp.append(board.game_objects[i].position)
                 

        if(self.countDistance(me.position,temp[0]) > self.countDistance(me.position,temp[1])):
             return temp[1]
        else:
             return temp[0]
        
    def isCloseBase(self, a:Position,b:Position):
        if(self.countDistance(a,b) <= 8):
            return True






    def next_move(self, board_bot: GameObject, board: Board):
        usPos = board_bot.position
        base = board_bot.properties.base
        time = (math.floor(board_bot.properties.milliseconds_left / 1000))
        print("waktu" , time)
        print("Jarak ke base " , self.countDistance(usPos,base))
        print(usPos)
        if(self.isDiamondAvailable(board)):
            bluePos = self.getClosestDiamondPos(board,board_bot)
         
        if(self.isRedAvailable(board)):
            redPos = self.getClosestRedPos(board,board_bot)
        if (time >= 15):
            if(board_bot.properties.diamonds == 5):
                delta_x,delta_y = self.goTo(usPos,base)
                print("Balik ke base (5)")

                #PROTOKOL MAIN AMAN DEKET BASE============
            elif(board_bot.properties.diamonds >= 3 and self.isCloseBase(usPos,base)) :
                if(self.isRedAvailable(board) and self.isDiamondAvailable(board)):
                    if (self.countDistance(usPos,redPos) < 3 and board_bot.properties.diamonds < 4):
                        print("pengen balik ke base tapi ada merah deket banget")
                        delta_x , delta_y = self.goTo(usPos,redPos)
                    elif(self.countDistance(usPos,bluePos) < 3):
                        print("pengen balik ke base tapi ada biru deket banget")
                        delta_x , delta_y = self.goTo(usPos,bluePos)
                    else:
                        print("Deket base dan ada diamond di invent")
                        delta_x, delta_y = self.goTo(usPos,base)
                else:
                    print("Deket base dan ada diamond di invent")
                    delta_x, delta_y = self.goTo(usPos,base)

                #PROTOKOL GAREP DIAMOND BANYAK======= 
            elif(board_bot.properties.diamonds <= 3):
                if(self.isDiamondAvailable(board) and self.isRedAvailable(board)):
                    if (self.countDistance(usPos,bluePos) < self.countDistance   (usPos,redPos)):
                        delta_x , delta_y = self.goTo(usPos,bluePos)
                        print("Prior Biru")
                    else:
                        delta_x , delta_y = self.goTo(usPos,redPos)
                        print("Prior Merah")
                elif(self.isDiamondAvailable(board) and self.isRedAvailable(board) == False):
                    delta_x,delta_y =  self.goTo(usPos,bluePos)
                    print("SIsa biru")
                else:
                    delta_x,delta_y = self.goTo(usPos,redPos)
                    print("SIsa merah")
            else:
                if(self.isDiamondAvailable(board)):
                    delta_x , delta_y = self.goTo(usPos,bluePos) 
                    print("Diamond ada 4 paksa ambil biru")    
                else:
                    delta_x,delta_y = self.goTo(usPos,base)
                    print("Diamond ada 4 tapi gk ada biru,balik") 
        else:
            if(board_bot.properties.diamonds > 0):
                delta_x , delta_y = self.goTo(usPos,base)
                print("Waktu dikit dan ada diamond,balik ke base")
            else:
                if(self.isDiamondAvailable(board) and self.isRedAvailable(board)):
                    if (self.countDistance(usPos,bluePos) < self.countDistance   (usPos,redPos)):
                        delta_x , delta_y = self.goTo(usPos,bluePos)
                        print("Prior biru waktu dikit")
                    else:
                        delta_x , delta_y = self.goTo(usPos,redPos)
                        print("Prior Merah waktu dikit")
                elif(self.isDiamondAvailable(board) and self.isRedAvailable(board) == False):
                    delta_x,delta_y =  self.goTo(usPos,bluePos)
                    print("SIsa biru waktu dikit")
                else:
                    delta_x,delta_y = self.goTo(usPos,redPos)
                    print("SIsa merah waktu dikit")
        return delta_x, delta_y


