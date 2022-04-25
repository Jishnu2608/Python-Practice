from collections import Counter
  
def minSubsets(input):
  
     freqDict = Counter(input)
   
     print (max(freqDict.values()))
  
# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 3]
    minSubsets(input)