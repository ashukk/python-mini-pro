from profanity_check import predict,predict_prob
fh=open('foo.txt','r')
string=fh.read()
a=predict([string])
if(a>=1):
  print("bad word found in string")
  print("amount of badwords in a string:",a)
  b=predict_prob([string])
  print("percentage of badness in the string:",b)
else:
    print("No bad words found") 
