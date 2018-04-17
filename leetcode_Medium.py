# 给定一个字符串 s，找到 s 中最长的回文子串
def long(s):
#开始用range(1,len(s)+1)，时间复杂度没有通过，由于是找最长回文字串所以倒着找更快
    for j in range(len(s),0,-1): 
        for i in range(len(s)-j+1):
            t = s[i:i+j]
            tr = t[::-1]
            if t == tr :
                return t