##あなたは今、とある戦略ゲームをプレイしています。
##ゲームの中で、敵を攻撃するために、フィールドに爆弾を仕掛けました。
##敵がフィールド内に入ったところで一気に爆弾を点火し、敵に攻撃をする寸法です。
##
##フィールドは縦 H 行、横 W 行のマス目としてあらわされ、これらのマス目のうちのいくつかに爆弾が仕掛けてあります。
##i 行目、j 列目の爆弾が爆発すると、i 行目全体と j 列目全体に爆風が広がります。
##図1
##
##あなたはすでにフィールド上に爆弾を仕掛け終わりました。
##フィールド上の爆弾を一気に点火した場合、いくつのマスに爆風が広がるかを計算してください。
##
##例えば、入力例 1 では以下のマスに爆風が広がるため、求めるべきマス目数は 12 になります。
##図1


#入力部
#入力された.と#を0,1に変換する
import numpy as np

a,b = input().split()
a = int(a)
b = int(b)

bomb_map = []
sublist =[]
result_map = [[0 for j in range(b)] for i in range(a)]
result = []


for i in range(a):
    x = list(input())
    for j in range (b):
        sublist.append(int ((ord(x[j]) - 46)/-11))
        #print(y)
    bomb_map.append(sublist)
    sublist =[]

    
#01の行列を規則に従って変換する

for i in range(a):
    for j in range (b):
        #print(j+i*b)
        if bomb_map[i][j] == 1:
            #print("xxx")
            #print(i,j)
            #print(len(result_map))
            #result_map[i][j] = 1
            for k in range(a):
                result_map[k][j] =1
                
            for l in range(b):
                result_map[i][l] =1

#新しい行列の全ての1を足して数を出力する
print(np.sum(result_map))



