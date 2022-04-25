# 0의 갯수 = 이전 1의 갯수
# 1의 갯수 = 이전 0의 갯수+이전 1의 갯수

tc = int(input())

for _ in range(tc):
    n=int(input())
    cnt_0=[1,0]
    cnt_1=[0,1]
    if n>1:
        for i in range(2,n+1):
            cnt_0.append(cnt_0[-1]+cnt_0[-2])
            cnt_1.append(cnt_1[-1]+cnt_1[-2])

    print(cnt_0[n], cnt_1[n])