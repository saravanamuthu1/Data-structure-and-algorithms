def sum_value(i):
    if i == 0 :
        return 0
    return i + sum_value(i-1)
def fibonnaci_num(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonnaci_num(n-1,b,a+b)
def reverse(s):
    if s == "":
        return s
    return s[-1] + reverse(s[:-1])

def gcd(a,b):
    if a%b == 0:
        return b
    gcd(b,a%b)
if __name__ == "__main__":
    print(fibonnaci_num(6))