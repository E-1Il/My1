#分數計算
#分數計算功能設計
#1.	設計簡單的分數計算器：輸入考試成績，程式自動計算平均分數。
#2.	加入錯誤處理：遇到非數字輸入時，提示「請輸入有效分數」。
#3.	每次修改後，使用 GitHub 進行版本管理，留下註解。
def calculate_average_score():
    scores = []
    while True:
        score_input = input("請輸入考試成績（輸入 'done' 結束）：")
        if score_input.lower() == 'done':
            break
        try:
            score = float(score_input)
            scores.append(score)
        except ValueError:
            print("請輸入有效分數")
    if scores:
        average_score = sum(scores) / len(scores)
        print(f"平均分數為: {average_score:.2f}")
    else:
        print("沒有輸入任何分數")
calculate_average_score()