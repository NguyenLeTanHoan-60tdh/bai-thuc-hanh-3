import math
r=int(input("nhap ban kinh" ))
if r>=0:
    cv = 2*math.pi*r
    dt = math.pi*r*r
    print("Chu vi hình tròn bằng: ", cv)
    print("Diện tích hình tròn bằng: ", dt)
else:
    print("ban kinh ko hop le")
