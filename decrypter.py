#decrypting
code1 = input('Enter the first code: ')
code2 = input('Enter the second code: ')
check = False
while(check == False):
  choice = input('Did the code have a zero at the beginning?(y/n)')
  if(choice == 'y' or choice == 'n'):
    check = True


slope = (int(code2)-int(code1))
print(f'\nThe slope of it is: {str(slope)}\n')
orignal = int(code1)-(int(slope))

if(choice == 'y'):
  orignal = '0' + str(orignal)
if(choice == 'n'):
	orignal = str(orignal)

print(f'The converted orignal text was {orignal}\n')
#print(len(str(pass1)))

va = ''
for i in range(len(orignal)):
  if(i%3==0):
    start = i
    end = i + 3
    va = str(va) + str(chr(int(orignal[start:end])))

print('The orignal text was: "' + va +'"')

with open('text.txt', 'w') as f:
  f.write('Orignal text: ' + va)
f.close()
