n=input()
sets=["a","e","i","o","u"]
set1=["!","@","#","$","%","&","*","(",")","=","+"]
if n in sets:
  print("Vowel")
elif n in set1:
  print("invalid")
else:
  print("Consonant")
