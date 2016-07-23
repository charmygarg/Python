# Type your code here
  
def find_mismatch(s1,s2):
    if len(s1)!=len(s2):
        return 2
    s1.upper()
    s2.upper()
    no_of_mismatch=0
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            no_of_mismatch=no_of_mismatch+1
                if no_of_mismatch>1:
                    return 2
     return no_of_mismatch
        
            