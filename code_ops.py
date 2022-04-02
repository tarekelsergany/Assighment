def find_nth_occurrence(substring, string, occurrence=1):
  try:
    import re
    x = re.finditer(substring , string)
    for match in x:
      y= match.group(),int(match.start())
      k = int(match.start())
      if occurrence==1:
            return k
      else:
          while occurrence >1:
              k = string.find(substring,k+1,len(string))
              occurrence-=1
      return k
      
  except:
    print("wrong,please try again")
#############################################################
def solve(a,b):
    try:
      if a == b:
            return True
      if "*" not in a :
            return False
      def split(word): 
          return [char for char in word]  
      x = split(a)
      y = split(b)
      x = set(x)
      y = set(y)
      z = y.difference(x)
      z = list(z)
      z = "".join(z)

      a=a.replace("*",z)
      a=sorted(a)
      b=sorted(b)
      if len(a)>len(b):
        return False
      if a==b:
        return True
      else:
        return False
    except:
        print("wrong,please try again")
###################################################################
def is_palindrome (s):
  try:
    x =s.lower()
    if x == x[::-1]:
        return True
    else:
        return False
  except:
    print("wrong,please try again")
is_palindrome("sdds")
########################################################################
def f(s):
  lst=[]
  for i in s:
    if i in lst:
      continue
    else:
      lst.append(i)
  x = "".join(lst)
  c = s.count(x)
  if c == 1:
    return(s,c)
  else:
    return(x,c)

f("aabababab")