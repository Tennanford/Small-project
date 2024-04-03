def pk(a,b,ap,bp): #a,b为种族，ap，bp为得分
    if a == b :
        if a == 0 :
            ap = ap + 1
            bp = bp + 1
        if a == 1 :
            ap = ap - 2
            bp = bp - 2
    if a != b :
        if a == 1 :
            ap += 2
        if b == 1 :
            bp += 2
            pass
        pass
    return ap, bp