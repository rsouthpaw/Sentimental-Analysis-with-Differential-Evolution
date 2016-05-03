#Various options are available in saving files. Use according to your need
#Last option is tested with the whole application. It works! :)

for xf in range(0, 99):
    xf=xf+1
    ftname='File'+str(xf)
    output=open(ftname+'.txt','w')

i=0
for i in range(0,100):        
    f = open("C:\Users\Saransh01\Desktop\Final\input_%i.txt" %i,'w')
    f.write(json.dumps(statuses[i], indent=1))
    i=i+1
    f.close()

i=0
f = open("C:\Users\Saransh01\Desktop\Power\kk.txt",'w')
for i in range(0,100):            
    f.write(json.dumps(statuses[i], indent=1))
    i=i+1


f.close()

f = open("Your_Path_Here\file_%i.data" %i,'w')
C:\Users\Saransh01\Desktop\Testing
    

	#mail id: saranshmiglani@gmail.com