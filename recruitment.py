def main():
	#write your code here
	print("Welcome to the special recruitment program, please answer the following questions:")
	uname = input("What's your name?")
	age = int(input("How old are you ?"))
	exp = int(input("How many years of experience do you have?"))

	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {
	'name':"" ,
	'age':"",
	'experience' :"" ,
	'skills' :[] ,
	}

	cv['name']= uname
	cv['age']= age
	cv["experience"]= exp
	i =1

	for skill in skills :
		print(f"{i}. " + skill)
		i += 1

	ski = int(input("Choose a skill from above by entering its number:"))
	#cv['skills'].append(skills[ski - 1])
	#print(cv.keys())
	#print(cv.values())
	ski2 = int(input("Choose another skill from above by entering its number:"))
	#cv['skills'].append(skills[ski2 - 1])

	cv['skills'] =  [skills[ski-1], skills[ski2-1]]
	#print(cv.keys())
	#print(cv.values())
	if cv['age'] >= 25 and cv['age'] <= 40 :
		if cv['experience'] > 5:
			if "Eating" in cv['skills']:
				print(f"You have been accepted, {uname}")
			else:
				print(f"You have been rejected, {uname}")
		else:
			print(f"You have been rejected, {uname}")
	else:
			print(f"You have been rejected, {uname}")




if __name__ == '__main__':
	main()
