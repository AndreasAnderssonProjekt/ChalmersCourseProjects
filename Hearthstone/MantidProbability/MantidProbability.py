import math
def mantid_prob_divine(t, N=3):
    M = [[0 for i in range(N+1)] for j in range(t+1)]
    M[0][0] = 1

    for i in range(1,t+1):
        for j in range(N+1):
            if j == 0:
                M[i][j] = M[i - 1][j] * (1 / (N-j + 1))
            else:
                M[i][j] = M[i-1][j] * (1/(N-j+1)) + M[i-1][j-1] *((N-j+1)/(N-j+2))

    divine_prob = 0
    for i in range(1,N+1):
        divine_prob += M[t][i] * (math.comb(N-1,i-1)/math.comb(N,i))
    return divine_prob
