"""
  
 計算1到1,000,000的數字加總,並列印出結果

"""
# 初始化
total = 0

# 使用range()產生1~1,000,000的數字序列
# 使用for in range(): 做數字序列的加總
for index in range(1, 1000001):
#    print(f"{index}:加總為: {total}")
    total = total + index
#    print(f"加總為: {total}")

# 印出加總結果
print(f"1到1,000,000的數字加總為: {total}")
