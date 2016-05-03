#Last option is tested and works well. Use options according to your need.

with open('C:\Users\Saransh01\Desktop\Testing2\input_1.txt', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        #tweet= line.decode('utf-8')
        tokens = preprocess(tweet['text'])
        do_something_else(tokens)

with open('C:\Users\Saransh01\Desktop\Testing2\input_1.txt', 'rb') as f:
    for line in f:
        if line.startswith(' "text":'):
            do_something_with_line(line)
            line.strip()
k=''
with open('C:\Users\Saransh01\Desktop\Power\kk.txt', 'rb') as f:
    for line in f:
        if line.startswith(' "text":'):
            p=line.strip()
            p.replace('"text": "',' ')
            k=k+p


            

            
#mail id: saranshmiglani@gmail.com