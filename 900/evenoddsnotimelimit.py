len, pos = list(map(int,input().split()))
kosz = []
if pos == 1 and len == 1:
    print(1)
    quit()
if pos <= len/2:
    print(pos*2-1)
    quit()
elif pos == len and (pos//2)*2 == pos:
    print(pos)
    quit()
elif pos == len and (pos//2)*2 == pos-1:
    print(pos-1)
    quit()
elif pos >= len/2 and pos*2-1==len:
    print(len)
    quit()
elif pos > len/2:
    if ((pos*2-len)//2)*2 != pos*2-len:
        print(pos*2-len-1)
    else:
        print(pos*2-len)
        quit()
