def mwc(list_len):
    a, i, r = 18782, 4095, 0xfffffffe
    i = (i + 1) & 4095
    t = a * q[i] + c
    c = (t >> 32)
    x = t + c
    if x < c:
        x, c = x + 1, c + 1
    return r - x
