import nltk

#///need to be run once///
#nltk.download() 

import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import numpy as np

def extract_keywords(msg):

    #   returns a list of keywords that are not present in stopwords   #

    #for optimization and incremention 
    
    bag={
    'about' : ['asmita','moghe','roopam','anjana','ratish','arpit','vikas','sachin','neera','ekta','shifa'],
    'location' : ['palce','position','site','where','location','dbms','lab','office','classroom','directions'],
    'syllabus' : ['syllabus','schema'],
    'notice' : ['notice','result','results','exam','notices','announcement','timetable', 'table','lectures','lecture','class','marks','score','events','schedule','scheme']
    }

    l=WordNetLemmatizer()
    ps=PorterStemmer()
    corpous = []
    temp = re .sub('[^a-zA-Z0-9]',' ',msg)
    temp = temp.lower()
    temp=temp.split()
    temp = [ps.stem(i) for i in temp if i not in stopwords.words('english')]
    # temp = ' '.join(temp)
    for word in temp :
        for k, v in bag.items():
            if word in v:
                corpous.append([k,word])
    return corpous

def reply(out,inp):
    if "@__@" in out:
            for i in range(-1,-100,-1):
                if out[i] == '@':
                    out=out[i-4::-1]
                    out=out[-1::-1]
                    break
            var=[out] + extract_keywords(inp)
            return var
    else:
        return out
