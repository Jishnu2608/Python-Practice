import requests 

def scrapeWords(): 
 
  scrape_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
  scrapeData = requests.get(scrape_url) 
  listofwords = scrapeData.content 
  listofwords = listofwords.decode("utf-8").split() 
  return listofwords 

def isOrdered():  
  collection = scrapeWords() 
  collection = collection[:100] 
  word = '' 

  for word in collection: 
    result = 'Word is ordered'
    i = 0
    l = len(word) - 1
    if (len(word) < 3):  
      continue
    while i < l:     
      if (ord(word[i]) > ord(word[i+1])): 
        result = 'Word is not ordered'
        break
      else: 
        i += 1 
    if (result == 'Word is ordered'): 
      print(word,': ',result) 

if __name__ == '__main__': 
  isOrdered()
  