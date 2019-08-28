def areanagrams(a,b):
    if((sorted(a))==(sorted(b))):
        return True
    else:
        return False
def countanagrams(text,words):
    N=text.length()
    n=words.length()
    res=0
    for i in range(0,(N-n)):
        k=text[i:i+n]
        if(areanagrams(words,k)):
            res+=1
    return res+1

text=input()
words=input()
print(countanagrams(text,words))
