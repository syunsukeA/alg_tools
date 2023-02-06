def gcd(a, b):
    if b == 0:
        print(a)
        return a
    else:
        return gcd(b, a%b)

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = gcd(n, m)
    print(g)