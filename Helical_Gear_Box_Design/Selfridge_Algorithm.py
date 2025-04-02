import math

R = 20
eps1 = 0.001 * R
eps = eps1
counter = 0
sol = [[0,0,0,0,0,0,0,0]]
N_min = 18
N_max = 100
s = 0
while(True):
    R_high = R + eps
    R_low = R - eps
    Nh3 = int(N_max**2/R_high)
    Nh4 = int(N_max/math.sqrt(R_high))
    for pinion1 in range(N_min,Nh4+1,1):
        Nhh = min(N_max,int(Nh3/pinion1))
        for pinion2 in range(pinion1,Nhh + 1,1):
            P = int(pinion1 * pinion2 * R_high)
            Q = int(pinion1 * pinion2 * R_low) + 1
            if (P < Q):
                s = s + 1
                continue
            Nm = max(N_min,int((Q + N_max - 1)/N_max))
            Np = int(math.sqrt(P))
            for K in range(Q,P+1,1):
                for gear1 in range(Nm,Np+1,1):
                    if (K % gear1 != 0):
                        s = s + 1
                        continue
                    gear2 = K/gear1
                    error = (R - K)/(pinion1 * pinion2)
                    if (error > eps):
                        s = s + 1
                        continue
                    else:
                        sol.append([pinion1,pinion2,gear1,gear2,abs(error),(gear1/pinion1),(gear2/pinion2),((gear1/pinion1)*(gear2/pinion2))])
    if (len(sol) == 0):
        eps = eps * 2
        counter = counter + 1
    else:
        print(sol[1])
        print(s)
        break

            
    
    
