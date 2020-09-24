# x== 0 and x== w -> x방향만 반대로
# y==0 and y == h -> y방향만 반대로
w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

S = (x + t) // w
G = (x + t) % w
if S % 2:
    X = w - G
else:
    X = G

print("{} {}".format(p, q))