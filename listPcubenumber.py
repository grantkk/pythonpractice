"""
  
 計算1到10的整數三次方,並列印出這些三次方的結果

"""
# 初始化串列
numbers = [" "] * 10

# 使用range()產生1~10的數字序列
# 使用for in range(): 做數字序列的三次方
for index in range(1, 11):
    number = index**3
    numbers[index - 1] = number

# 印出整個串列結果
for index in range(0, 10):
    print(f"{index+1 : >2}的三次方:{numbers[index] : >4}")
