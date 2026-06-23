print("Answer only yes or no")
q1=input("1.Did you recieve a message saying you won a prize?:")
q2=input("2.Did you recieve a suspicious link?:")
q3=input("3.Did an unknown number call you receive repeatedly?:")
q4=input("4.Did the message ask for your bank details or OTP?:")
q5=input("5.Did the caller or message create urgency?:")
if(q1.lower()=="yes" or
   q2.lower()=="yes" or
   q3.lower()=="yes" or
   q4.lower()=="yes" or
   q5.lower()=="yes"):
    print("\n Prediction:Possible Spam")
else:
    print("\n Prediction:Safe")
