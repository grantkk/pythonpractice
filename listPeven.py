"""
  
 計算1到1,000,000的偶數加總,並列印出結果

"""
# 初始化
total = 0

# 使用range()產生1~1,000,000的偶數序列
# 使用for in range(): 做數字序列的加總
for index in range(2, 1000001, 2):
    total = total + index

# 印出加總結果
print(f"1到1,000,000的偶數加總為: {total}")
