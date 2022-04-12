def MaxSubSquare(M):
    R = len(arr1) 
    C = len(arr1[0]) 

    S = [[0 for k in range(C)] for l in range(R)]

    for i in range(1, R):
        for j in range(1, C):
            if (arr1[i][j] == 1):
                S[i][j] = min(S[i][j-1],S[i-1][j],S[i-1][j-1])+1
            else:
                S[i][j] = 0

    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print (arr1[i][j], end = " ")
        print("")

arr1 = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]

MaxSubSquare(arr1)