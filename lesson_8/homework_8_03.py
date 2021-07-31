def sin1(x, e):
    if x > 0 and e > 0:
        an = x
        result = 0
        z = 1
        n = z
        while an > e:
            result += z * an
            an *= x*x/(n + 1)*(n+2)
            n += 2
            z = -z
        return result
    else:
        return -1
print(sin1(0.5, 0.01))

