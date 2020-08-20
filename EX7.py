n = int(input())  # 輸入好友個數
data = input()
list = data.split(' ')  # 將好友編號分開
w = []  # 記錄好友編號
v = []  # 記錄是否追蹤過
flag = 0  # 小群體個數
w = [int(x) for x in list]  # 將輸入的字串變整數
for i in range(n):
    v.append(0)  # 一開始都沒追蹤，設為0

for j in range(n):
    if v[j] == 0:  # 從沒追蹤的開始追蹤，追蹤過的變為1
        if w[j] == j:  # 自己是自己的好友，算一個小群體
            flag += 1  # 小群體直接加1
            v[j] = 1  # 追蹤過的變為1
        else:  # 有其它人為好友
            nextone = j  # 用nextone來當暫存數
            while v[nextone] == 0:  # 當沒拜訪過就繼續拜訪
                v[nextone] = 1  # 拜訪過的變為1
                nextone = w[nextone]  # 一直循環到成一小群體
            flag += 1  # 成一小群體加1

print(flag)  # 印出小群體個數