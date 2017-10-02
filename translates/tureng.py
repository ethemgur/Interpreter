#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib.request,argparse
from bs4 import BeautifulSoup as bs

# Emre Ovunc
# info@emreovunc.com

uList = ['Turkish English Dictionary','German English Dictionary','Spanish English Dictionary','French English Dictionary','English Synonyms Dictionary','Privacy Policy','Terms of Use','About Us','Contact','None','Turkish - English','German - English','French - English','Spanish - English','English Synonyms','English','Deutsch','Translation','Synonyms','Tools','Resources','None','Turkish - English','German - English','Spanish - English','French - English','English Synonyms','Turkish - English','French - English','Spanish - English','German - English']
tr_Error = ['&#231;','&#246;','&#252;','&#160;','&#39;']
fix = ['c','o','u','','\'']

def arg_parse():
    parser = argparse.ArgumentParser(description='Tureng Machine | Emre Ovunc')
    parser.add_argument("-w",'--word', required=True,help='enter a word to convert')
    parser.add_argument("-v",'--version', action='version', version='TurengMachine v1.0')
    args = parser.parse_args()
    return args.word

def Tureng(word):
    f = urllib.request.urlopen("http://tureng.com/en/turkish-english/"+str(word))
    soup = bs(f, "html.parser")
    dummy=0
    emocan = 0
    count = 0
    max_count = 10
    translations = []
    for string in soup.findAll('a'):
        if int(dummy) > 20 and count < max_count:
            wflag = 0
            for x in range (0,len(uList)):
                if string.string == uList[x]:
                    wflag=1
                    break
            if wflag == 0:
                if string.string is not None:
                    for tr in range(0, len(tr_Error)):
                        if tr_Error[tr] in string.string:
                            string.string = string.string.replace(tr_Error[tr], fix[tr])
                    if emocan == 0:
                        try:
                            print("1",string.string.decode('utf-8'),' ---> ',)
                        except:
                            print("2",string.string,' ---> ',)
                        emocan=1
                    else:
                        count += 1
                        try:
                            print("3",string.string.decode('utf-8'))
                            translations.append(string.string.decode('utf-8'))
                        except:
                            print("4",string.string)
                            translations.append(string.string)
                        emocan=0
        dummy+=1

    for i in translations:
        print(i)
    return translations

def main():
    word = arg_parse()
    Tureng(word)

if __name__ == "__main__":
    main()
