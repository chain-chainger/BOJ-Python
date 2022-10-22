def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split(':'))
gcd_nm = gcd(n, m)
print(f"{n // gcd_nm}:{m // gcd_nm}")