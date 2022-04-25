def answer(X, K):
      
    # Computing MAX
    MAX = pow(10, K) - 1
      
    #returning ans
    return (MAX - (MAX % X))
  
X = int(input("Enter X: "))
K = int(input("Enter K: "))
  
print(answer(X, K))
