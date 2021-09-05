#あなたは某 P 社のセキュリティ部門で働くエンジニアです。あなたは今、会社の入口に設置する特殊な認証システムの開発を行っています。

#今回作る認証システムでは、英小文字の文字列で表される合言葉が使われます。

#認証システムは、毎回誰かが会社に入ろうとしたときに、合言葉の入力を要求します。このとき、合言葉をそのまま入力すると、「合言葉が流出した」と判断され、認証エラーとして会社の入り口をロックしてしまいます。そのため、会社に入るには、合言葉の文字の並びを入れ替えて、合言葉そのものとは一致しない文字列を入力する必要があります。それ以外の文字列を入力した場合も認証エラーとなってしまい、会社に入ることが出来ません。

#「合言葉」と認証システムに入力される文字列が与えられたときに、その文字列で会社に入れるかどうかを判定するプログラムを作成してください。

#入力例 1 〜 3 では、「合言葉」は "abc" です。

#・入力例 1の場合、システムに入力される文字列は "bac" です。この 2 つの文字列は一致していませんが、"abc" の 1 文字目と 2 文字目を入れ替えれば "abc" になるので、この場合は会社に入ることが出来ます。
#・入力例 2 の場合、システムに入力される文字列は "abc" です。この 2 つの文字列は一致しているため、認証エラーになってしまい会社に入ることは出来ません。
#・入力例 3 の場合、システムに入力される文字列は "xy" です。この 2 つの文字列は一致していませんが、"xy" をどのように入れ替えても "abc" と一致させることが出来ないので、認証エラーになってしまい会社に入ることは出来ません。

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
t = input()
c = 0

if s == t:
    print("NO")
else:
    a = s.count('a')
    b = t.count('a')
    if a != b :
        c = 1
    else:
        a = s.count('b')
        b = t.count('b')
    if a != b :
        c = 1
    else:
        a = s.count('c')
        b = t.count('c')
    if a != b :
        c = 1
    else:
        a = s.count('d')
        b = t.count('d')
    if a != b :
        c = 1
    else:
        a = s.count('e')
        b = t.count('e')
    if a != b :
        c = 1
    else:
        a = s.count('f')
        b = t.count('f')
    if a != b :
        c = 1
    else:
        a = s.count('g')
        b = t.count('g')
    if a != b :
        c = 1
    else:
        a = s.count('h')
        b = t.count('h')
    if a != b :
        c = 1
    else:
        a = s.count('i')
        b = t.count('i')
    if a != b :
        c = 1
    else:
        a = s.count('j')
        b = t.count('j')
    if a != b :
        c = 1
    else:
        a = s.count('k')
        b = t.count('k')
    if a != b :
        c = 1
    else:
        a = s.count('l')
        b = t.count('l')
    if a != b :
        c = 1
    else:
        a = s.count('m')
        b = t.count('m')
    if a != b :
        c = 1
    else:
        a = s.count('n')
        b = t.count('n')
    if a != b :
        c = 1
    else:
        a = s.count('o')
        b = t.count('o')
    if a != b :
        c = 1
    else:
        a = s.count('p')
        b = t.count('p')
    if a != b :
        c = 1
    else:
        a = s.count('q')
        b = t.count('q')
    if a != b :
        c = 1
    else:
        a = s.count('r')
        b = t.count('r')
    if a != b :
        c = 1
    else:
        a = s.count('s')
        b = t.count('s')
    if a != b :
        c = 1
    else:
        a = s.count('t')
        b = t.count('t')
    if a != b :
        c = 1
    else:
        a = s.count('u')
        b = t.count('u')
    if a != b :
        c = 1
    else:
        a = s.count('v')
        b = t.count('v')
    if a != b :
        c = 1
    else:
        a = s.count('w')
        b = t.count('w')
    if a != b :
        c = 1
    else:
        a = s.count('x')
        b = t.count('x')
    if a != b :
        c = 1
    else:
        a = s.count('y')
        b = t.count('y')
    if a != b :
        c = 1
    else:
        a = s.count('z')
        b = t.count('z')
    if a != b :
        c = 1
    else: 
        print ("YES")
    if c == 1:
        print ("NO")