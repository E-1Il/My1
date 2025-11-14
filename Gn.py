# 猜數字遊戲
import random
def guess_number_game():
# 猜數字遊戲規則與步驟
#• 隨機產生一個1到100的整數答案。
#• 玩家每次輸入猜測數字，節目提示「大了」或「小了」。
#• 回答時「恭喜通過！」結束並遊戲。
#• 節目需記錄猜測次數，顯示學員的持續進度。
#以Python完成此練習，將節目碼上傳至自己的GitHub倉庫，記錄顯示每次修改。
    answer = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！請猜一個1到100之間的數字。")
    while True:
        guess_input = input("請輸入你的猜測（或輸入 'exit' 結束遊戲）：")
        if guess_input.lower() == 'exit':
            print(f"遊戲結束，正確答案是 {answer}。")
            break
        try:
            guess = int(guess_input)
            attempts += 1
            if guess < answer:
                print("小了！再試一次。")
            elif guess > answer:
                print("大了！再試一次。")
            else:
                print(f"恭喜通過！你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入有效的整數數字。")
guess_number_game()