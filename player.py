from agent import Agent
import pygame


class PlayerAgent(Agent):
    def __init__(self, side):
        """
        --------------------------------------------------------
        #### 物件 : 玩家
        --------------------------------------------------------
        #### 函式
        - isOnCorner() : 根據輸入的位置判斷是否在棋盤的角落
        - isOnBorder() : 根據輸入的位置判斷是否在棋盤的邊緣
        - choose() : 判斷玩家滑鼠點擊的位置是否能下，若能則玩家的棋子下在此處
        --------------------------------------------------------
        #### 傳入的參數
        - side : 玩家拿的棋子顏色 (以字串型態表示 : "black"或"white")
        --------------------------------------------------------
        #### 物件中的屬性
        - side : 玩家拿的棋子顏色
        - name : 玩家名稱，在此處皆命名成"human"
        - opponentSide : 對手的棋子顏色
        --------------------------------------------------------
        """
        super().__init__(side) # 繼承agent
        self.name = "human"

    def choose(self, board, valid_moves):
        """
        --------------------------------------------------------
        #### 功能 : 判斷玩家滑鼠點擊的位置是否能下，若能則玩家的棋子下在此處
        --------------------------------------------------------
        #### 參數
        - board : 棋盤
        - valid_moves : 目前可以下的位置 (資料型態 : 陣列)
        --------------------------------------------------------
        #### 回傳值
        - 含有兩個元素的陣列，表示最後選擇的位置 ; 若沒有選擇, 回傳None
        --------------------------------------------------------
        """
        x, y = pygame.mouse.get_pos()  # 取得滑鼠點擊的位置
        col, row = int((x - 20) / 50), int((y - 20) / 50)  # 計算在棋盤上的位置 (0~7)
        if [col, row] in valid_moves:
            return [col, row]
        else:
            return None