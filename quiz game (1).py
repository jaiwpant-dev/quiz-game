# quiz game ...
score=0
print("Quiz Game")
q1=" Q1. who is the pm of india :"
print(q1)
a1=input("")
a="Narendra modi"
if a1==a:
	print(" (correct)")
	score+=1
else :
		print("(incorrect)")
		
q2="Q 2. name smallest even prime no"
print(q2)
a2=int(input(""))
a= 2
if a2==a:
	print("(correct)")
	score+=1
else:
	print("(incorrect)")

q3="Q 3. name the national animal of india"
print(q3)
a3=input("")
a="tiger"
if a3==a:
	print("(correct)")
	score+=1
else:
	print("(incorrect)")

q4="Q 4. when did india got freedom"
print(q4)
a4=int(input(""))
a=1947
if a4==a:
	print("(correct)")
	score+=1
else:
	print("(incorrect)")
	
q5="Q 5. what is the name of our planet"
print(q5)
a5=input("")

a="earth"
if a5==a:
	print("(correct)")
	score+=1
else:
	print("(incorrect) ")
	
	print("Your score : ", score)
		
	if score==0:
		print(" very poor")
	elif score==1:
		print("need improvemt")
	elif score==2:
		print("can do better")
	elif score==3:	
	    print("good")
	elif score==4:
	   print("very nice")    	
	elif score==5:
	   print("excellence")
	

print("thanks for playing")