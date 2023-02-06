def base_xto10(str_n, x=8):
    ans = 0
    for i in range(len(str_n)):
        ans += int(str_n[-(i+1)]) * x**i
    return str(ans)

"""
    pythonだと文字列はイミュータブルなので毎回文字列を作ることになるのでこの方法だとあまり良くないかも？
    でもhシンプルなのでまぁこれでいい気もする。O(logn^3)??
"""
# def base_10tox(str_n, x=9):
#     ans = ''
#     n = int(str_n)
#     while n > 0:
#         ans = str(n%9) + ans
#         n//=x
#     return ans

"""pythonならこっちの方が計算量的に早い O(logn)"""
def base_10tox(str_n, x=9):
    i = 0
    n = int(str_n)
    while n//x**i > 0: i += 1
    ans = ['0']*i
    while i > 0:
         ans[-i] = str(n//x**(i-1))
         n %= x**(i-1)
         i -= 1
    return "".join(ans)