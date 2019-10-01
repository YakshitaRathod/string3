#To find the number of occurance of each character present in string
s=input("Enter the string:")
out=[]
for x in s:
	if x not in out:
		out.append(x)
for cou in out:
	print("The occurance of {} is {}".format(cou,s.count(out)),)
