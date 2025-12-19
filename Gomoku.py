# 五子棋遊戲
# 五子棋（Gomoku）遊戲規則與實作

# 遊戲常數
BOARD_SIZE = 15  # 標準五子棋棋盤大小

# 五子棋介紹：
# 五子棋是一種兩人對弈的策略棋盤遊戲，起源於中國古代。
# 英文名稱為 Gomoku 或 Five in a Row（五子連珠）。

# 遊戲規則：
# 1. 棋盤：通常使用15x15的方格棋盤（也有19x19的版本）
# 2. 棋子：兩位玩家分別使用黑色和白色棋子，黑方先行
# 3. 勝利條件：先在橫向、縱向或斜向連成五個相同顏色的棋子即獲勝
# 4. 下棋規則：玩家輪流在棋盤的空位上放置自己的棋子
# 5. 禁手規則：某些版本有禁手規則，限制黑方的某些走法（本實作採用自由規則）

# 策略技巧：
# • 進攻：嘗試構建連續的棋子，形成活三、活四等優勢局面
# • 防守：阻擋對手的連珠，防止對手先達成五連
# • 雙重威脅：同時建立多個進攻路線，讓對手無法同時防守

def print_board(board):
    """
    印出棋盤狀態
    :param board: 二維列表代表棋盤
    """
    print("\n  ", end="")
    for i in range(len(board[0])):
        print(f"{i:2}", end=" ")
    print()
    
    for i, row in enumerate(board):
        print(f"{i:2}", end=" ")
        for cell in row:
            if cell == 0:
                print("·", end="  ")  # 空位
            elif cell == 1:
                print("●", end="  ")  # 黑子
            else:
                print("○", end="  ")  # 白子
        print()
    print()

def check_winner(board, row, col, player):
    """
    檢查是否有玩家獲勝（五子連珠）
    :param board: 棋盤
    :param row: 最後下棋的行
    :param col: 最後下棋的列
    :param player: 玩家編號（1或2）
    :return: True 如果該玩家獲勝，否則 False
    """
    directions = [
        (0, 1),   # 水平
        (1, 0),   # 垂直
        (1, 1),   # 右下斜
        (1, -1)   # 左下斜
    ]
    
    for dx, dy in directions:
        count = 1  # 包含當前棋子
        
        # 檢查正方向
        i, j = row + dx, col + dy
        while 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == player:
            count += 1
            i += dx
            j += dy
        
        # 檢查反方向
        i, j = row - dx, col - dy
        while 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == player:
            count += 1
            i -= dx
            j -= dy
        
        if count >= 5:
            return True
    
    return False

def is_board_full(board):
    """
    檢查棋盤是否已滿
    :param board: 棋盤
    :return: True 如果棋盤已滿，否則 False
    """
    for row in board:
        if 0 in row:
            return False
    return True

def gomoku_game():
    """
    五子棋遊戲主程式
    """
    # 初始化棋盤
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    current_player = 1  # 1 代表黑子，2 代表白子
    player_names = {1: "黑方(●)", 2: "白方(○)"}
    
    print("=" * 50)
    print("歡迎來到五子棋遊戲！")
    print("=" * 50)
    print("\n遊戲規則：")
    print("• 兩位玩家輪流下棋，黑方先行")
    print("• 在橫、縱或斜方向連成五子即獲勝")
    print("• 輸入座標格式：行 列（例如：7 7）")
    print("• 輸入 'exit' 可以退出遊戲")
    print("=" * 50)
    
    print_board(board)
    
    while True:
        print(f"\n輪到 {player_names[current_player]} 下棋")
        move_input = input("請輸入座標（行 列）或輸入 'exit' 退出：").strip()
        
        if move_input.lower() == 'exit':
            print("遊戲結束，感謝遊玩！")
            break
        
        try:
            parts = move_input.split()
            if len(parts) != 2:
                print("請輸入正確的格式：行 列（例如：7 7）")
                continue
            
            row, col = int(parts[0]), int(parts[1])
            
            # 檢查座標是否有效
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                print(f"座標超出範圍！請輸入 0 到 {BOARD_SIZE-1} 之間的數字。")
                continue
            
            # 檢查位置是否已被佔據
            if board[row][col] != 0:
                print("該位置已有棋子，請選擇其他位置！")
                continue
            
            # 放置棋子
            board[row][col] = current_player
            print_board(board)
            
            # 檢查是否獲勝
            if check_winner(board, row, col, current_player):
                print("=" * 50)
                print(f"🎉 恭喜！{player_names[current_player]} 獲勝！🎉")
                print("=" * 50)
                break
            
            # 檢查是否平局
            if is_board_full(board):
                print("=" * 50)
                print("棋盤已滿，平局！")
                print("=" * 50)
                break
            
            # 切換玩家
            current_player = 2 if current_player == 1 else 1
            
        except ValueError:
            print("請輸入有效的整數座標！")
        except Exception as e:
            print(f"發生錯誤：{e}")

# 執行遊戲
if __name__ == "__main__":
    gomoku_game()
