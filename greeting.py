print ('What is your name?')
name = input()
print ('What is your age?')
age = input()
print(name,age)

next_year_age = int(age) + 1
greeting = 'Yo, ' + name + '!'
next_year_reminder = 'Damn you outdated meme! Next year, you will be ' + str(next_year_age) + '!'

print(greeting)
print(next_year_reminder)
