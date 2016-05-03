#All the preprocessing is done here
#Uses nltk

from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
hash_re= re.compile(r'#.*', re.VERBOSE | re.IGNORECASE)
stop = stopwords.words('english') + punctuation + ['rt', 'via','RT','u\'rt','u',':/','://'':\\']


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

#with open('C:\Users\Saransh01\Desktop\Power\pp.txt','rb') as fin, open('C:\Users\Saransh01\Desktop\Power\pp2.txt','wb') as fout:
with open("C:\Users\Saransh01\Desktop\Power\pp.txt", "r") as ins:
    your_list = []
    for line in ins:
        your_list.append(line)
#fin=open('bjptwetutf8encoding.csv','rb')
#reader = reader(fin) 
    #writer = Writer(fout,quoting=csv.QUOTE_ALL)
#your_list=list(fin)
str1 = ''.join(str(e) for e in your_list)  #converting list to string
str2=str1.replace('[','').replace(']','\n')  #removing all braces [] from list.
str2=str2.lower()


		
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens		

#with open('emoticons.csv', mode='r') as infile: 
#        reader = csv.reader(infile)
   # with open('coors_new.csv', mode='w') as outfile:
        #writer = csv.writer(outfile)
        #mydict = dict((rows[0],rows[1]) for rows in reader)

#def comparator(word):
#	if word in mydict:
#		temp = mydict[word]
#		return temp	
#	else:
#		return word
		
terms_stop = [term for term in preprocess(str2) if term not in stop]
terms_hash = [term for term in terms_stop if not term.startswith('#')]
#terms_hash = [mydict[term] if (term in mydict) else term for term in terms_hash]
terms_hash = [term if not term.startswith('u\'') else term[2:] for term in terms_hash]
terms_hash = [term for term in terms_hash if not (term.startswith('@') or term.startswith('u0') or term.startswith('u1') or term.startswith('u2') or term.startswith('w0rd') or term.startswith('\\x'))]
terms_hash = [term for term in terms_hash if not (term.startswith('htt') or term.startswith('u\'htt') or term.startswith(':/') )]
pass1=terms_hash

#save file in cmd not written fcode
print(pass1)	

#mail id: saranshmiglani@gmail.com
