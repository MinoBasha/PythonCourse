#Beginner (I)

def task_one(message):
	vowels = ("a","A","e","E","i","I","o","O","u","U")
	new_message = ""
	for letter in message:
		if letter not in vowels:
			new_message+=letter
		# if letter in vowels:
		# 	print("el 7arf",letter,"vowel ya me3alem")
	return new_message


#Beginner (II)

def task_two(word,letter):
    myList = []
    counter = 0
    for i in word:
        if letter == i:
            myList.append(counter)
        counter += 1
    return myList

##another code
# def task_two(message,letter1):
# 	posOfLetter1 = []
# 	counter=0
# 	for letter2 in message:
# 		if(letter2==letter1):
# 			posOfLetter1.append(counter)
# 		counter+=1
# 	print(posOfLetter1)

#Intermediate (I)
def task_three(number):
	list_one = []
	list_two = []
	number = int(number)
	for i in range(1, number + 1):
		for j in range(1, i + 1):
			list_two.append(i*j)
		list_one.append(list_two)
		list_two=[]
	return list_one

#Intermediate (II)
import math
def task_four(type,num1,num2=1):
    if type =='t' or type=='T':
        area= 0.5*num1*num2
    elif type =='r' or type=='R':
        area= num1*num2
    elif type =='c' or type=='C':
        area=math.pi*(num1**2)
    elif type =='s' or type=='S':
        area=num1**2
    else:
        area=0
    return area

#Advanced

def task_five(names):
    names.sort()
    result = {}
    for name in names:
        if name[0] in result:
            result[name[0]].append(name)
        else:
            result[name[0]] = [name]
            # result[name[0]].append(name)
    return result

##another code
#new_list={}
#old_list=["Mina","Hossam","Abdo","Ali"]
#old_list.sort()
#for letter in range(len(old_list)):
#	new_list[old_list[letter][0]]=old_list[letter]
#print(new_list)


#Mario Pyramid

# number=input("ekteb el rakam: ")
# rang=range(int(number))
# for i in rang:
# 	print(" "*(int(number)-1-i) + "*"*(i+1))
