def safe_division(a, b):
    """
    安全除法函式，當分母b為0時返回None，否則返回a/b的結果。
    :param a: 被除數
    :param b: 除數
    :return: a / b 或 None（如果 b 為 0）
    """
    if b == 0:
        print("錯誤：除數不能為零，請重新輸入。")
        return None
    return a / b

# 範例用法
result = safe_division(10, 0)  # 輸出: 錯誤：除數不能為零，請重新輸入。 result = None
print("結果:", result)

result2 = safe_division(10, 2) # result2 = 5.0
print("結果:", result2)
