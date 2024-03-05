name=input("Enter your name:")
print("Welcome to KBC",name)
print("10 question will be asked.If you answer all of them correctly you will win ONE CORE")

li=[
    "Q1. What is the capital of Nepal?\n A) Kathmandu B) Pokhara C) Biratnagar D) Birgunj",
    "Q2.Which is the smallest district in nepal?\nA)jhapa B)Rukum C)Lalitpur D)Rupandehi",
    "Q3.What is the national animal of nepal?\nA)Tiger B)Buffalo C)Bull D)Cow",
    "Q4.What is the national flower of nepal?\nA)Marigold B)Lily C)Rododendon D)Rose",
    "Q5.What is the height of mount everest\nA)2290 B)1024 C)8484 D)8848",
    "Q6.Who is the current prime minister of nepal?\nA)KP oli B)Pranchanda C)Ravi",
    "Q7.what is the current Population of nepal?\nA)10M B)20M C)30M D)43M",
    "Q8.what is the national sport of Nepal?\nA)Cricket B)Football C)Batminton D)volleyball",
    "Q9.When was the constitution of nepal passed?\nA)2015 B)2011 C)2008 D)2022",
    "Q10.How many provelegence are there in nepal?\nA)12 B)7 C)5 D)8",
     ]
li2=["A","C","D","C","D","B","C","D","A","B"]

score=0
for i in range(0,len(li)):
   user_answer = input(li[i] + "\n").upper()
   if user_answer in li2[i]:
        print("Correct!")
        score += 1
   else:
      print("Incorrect!")



print("You scored", score, "out of", len(li),"congratulation on winning 1 core")

