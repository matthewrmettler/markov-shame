import glob
import re
import random
import os

dict = {}
def add_to_dictionary(file):
    global dict
    with open(file, 'r') as f:
        text = f.read().lower()
        text = re.sub(ur"[^\w\d'\s]+", " ", text)
        words = list(text.split())
        for i in range(len(words)-2):
            key = str(words[i] + " " + words[i+1])
            dict.setdefault(key, [])
            dict[key].append(words[i+2])

def generate_chain(length):
    ##print('generate_chain')
    #print(len(dict))
    sentence = ''
    rkey = random.choice(dict.keys())
    rphrase = random.choice(dict[rkey])
    sentence += rkey + " " + rphrase
    rkey = str(rkey.split(' ')[-1] + " " + rphrase)
    for i in range(length-1):
        if rkey in dict:
            rphrase = random.choice(dict[rkey])
        else:
            rphrase = random.choice(dict[random.choice(dict.keys())])
        sentence += " " + rphrase
        rkey = str(rkey.split(' ')[-1] + " " + rphrase)
    #print(sentence)
    return sentence

def getChainForPolitician(pol):
    root = root_dir()
    scripts = "/transcripts/{0}".format(pol)
    src = root + scripts
    print(src)
    if os.path.isdir(src):
        for item in glob.glob("{0}/*.txt".format(src)):
            #print(item)
            add_to_dictionary(item)
        return generate_chain(50)
    else:
        print("Can't find directory!")
        return False

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))