def encryption(key,msg):
  mapkey={}
  temp=0
  for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    mapkey[j]=key[temp]
    temp+=1
  for j in msg:
   print(mapkey[j])

def decryption(key,msg):
   mapkey={}
   temp=0
   for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      mapkey[j]=key[temp] 
      temp+=1
   for j in msg:
      print([k for k,v in mapkey.items() if v == j])

key=input("please enter key=")
msg=input("please enter msg=")

e=encryption(key,msg)
print(e)
d=decryption(key,msg)
print(d)
