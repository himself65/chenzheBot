from random import randint


def distance(a, b): return 0 if a == b else 1


def dtwDistance(a, b):
    """
    Dynamic Time Warp
    >>> dtwDistance("chenzhe强啊", "chenzhe好好强啊")
    """
    if not isinstance(a, (str)) or not isinstance(b, (str)):
        # check if a or b are string
        raise ValueError
    MAX_COST = 1 << 32
    lena = len(a)
    lenb = len(b)
    dtw_array = [[MAX_COST for i in range(lena)] for j in range(lenb)]
    dtw_array[0][0] = distance(a[0], b[0])
    for i in range(lenb):
        for j in range(lena):
            if i+j == 0:
                continue
            nb = []
            if i > 0:
                nb.append(dtw_array[i-1][j])
            if j > 0:
                nb.append(dtw_array[i][j-1])
            if i > 0 and j > 0:
                nb.append(dtw_array[i-1][j-1])
            minr = min(nb)
            cost = distance(a[j], b[i])
            dtw_array[i][j] = cost + minr
    return dtw_array[lenb-1][lena-1]


if __name__ == '__main__':
    s1 = "chenzhe好强"
    s2 = "chenzhe好强"
    s3 = "chenzhe好强啊"
    s4 = "chenzhe是真真真真真真的强"
    d1 = dtwDistance(s1, s2)
    d2 = dtwDistance(s1, s3)
    d3 = dtwDistance(s1, s4)
    print(d1, d2, d3)
