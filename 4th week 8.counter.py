"""Write a function that takes an input from user and than gives the number of upper case letters and smaller case 
letters of it.
	For example : 
		function call: counter("asdASD")
		output: smaller letter : 3
		upper letter : 3"""""

def counter(s):  #We define a function counter.
  uppers = 0     #we fistly begin 0 for uppers and lowers letters
  lowers = 0
  for c in s:    #We set for loop for scanning letters.
    if c.islower(): #If it is lower, we add its to lowers
      lowers += 1
    elif c.isupper():  #And if it is upper,We add its to uppers
      uppers +=1
    else: #I added an extra conditoin for the rest of the charchter that aren't lower and upper
      pass
  return "upper letter is:",uppers,"\n","lower letter is:",lowers #We finally  print numbers of lower and upper letters

print(*counter('asdfggYUJF7'))