#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 02:55:22 2019

@author: ovishake
"""

import xml.etree.ElementTree as et

malenames = ["luke", "ted", "david", "matthew", "jake", "rick", "josh","tony", "aaron", "michael", "nick", "george", "john"]

femalenames =[
    "judith",
    "tia",
    "meg",
    "vicky",
    "eva",
    "july",
    "rita",
    "leah",
    "caroline",
    "cintihia",
    "ariel",
    "macy",
    "lynn",
    "rebecca",
    "cinthia",
    "mara",
    "amy",
    "michelle"
]


'''
Hash Maps for keeping the tags of pronouns
'''

male_placeholder = {
        "luke":0,
        "ted":0,
        "david":0,
        "matthew":0,
        "jake":0,
        "rick":0,
        "josh":0,
        "tony":0,
        "aaron":0,
        "michael":0,
        "nick":0,
        "george":0,
        "john":0
        }

female_placeholder ={
    "judith":0,
    "tia":0,
    "meg":0,
    "vicky":0,
    "eva":0,
    "july":0,
    "rita":0,
    "leah":0,
    "caroline":0,
    "cintihia":0,
    "ariel":0,
    "macy":0,
    "lynn":0,
    "rebecca":0,
    "cinthia":0,
    "mara":0,
    "amy":0,
    "michelle":0
}





#./root/document/sentences/tokens

#tree = et.ElementTree(file='Feb28_GroupA.txt.xml')

tree = et.parse('Feb28_GroupB.txt.xml')

'''
    ElementTree:
        get the root and check for names from the list malenames
    child:
        Child element of the root
    docm:
        documents inside the root
    sents:
        sentences inside the document
    sent:
        gets a collection of tokens, which are inside sentence, as a result if 
        you do a find('tokens') you will get the tokens inside it
    male_placeholder:
        the hashmap for holding the count of pronouns
'''

root = tree.getroot()
for names in malenames:
    for child in root:
        for docm in child:
            for sents in docm:
#                print sent
                for sent in sents:
                    '''just crossed the sentence and is at the tokens'''
                    name = sent[0][0].text
#                    print name
                    if name == names:
#                        i=0
                        for tokn in sent.findall('token'):
                            for tk in tokn.findall('POS'):
                                if tk.text == 'PRP' or tk.text == 'PRP$':
#                                    i = i + 1
#                                    print tk.text
                                    male_placeholder[names]= male_placeholder[names] + 1
                            
                        
                
print male_placeholder
#                    if name == names:
                        
#                    for tokn in sent.findall('token'):
#                        '''
#                        GIVES ALL BELOW THE TOKEN
#                        '''
                        
#                        print tokn.attrib
                        
#                        if tokn.attrib == '{'id': '1'}':
#                            print tokn.find('word').text
    ##                    print tok.tag
    #                    for tk in tok:
    ##                        print tk.tag
    #                        name = tk.find('word').tag
    #                        pronoun = tk.find('POS').tag
    #                        print name
    #                        print pronoun
                        
#                        name = tokn.find('word').text
#                        pronoun = tokn.find('POS').text
#                        if name == names and tokn.attrib == '1':
##                        if (pronoun == 'PRP' or pronoun == 'PRP$'):
#                            print name
#                        if tokn.attrib == '1':
#                            print tokn.find('word').text
    
    
'''
    ElementTree:
        get the root and check for names from the list malenames
    child:
        Child element of the root
    docm:
        documents inside the root
    sents:
        sentences inside the document
    sent:
        gets a collection of tokens, which are inside sentence, as a result if 
        you do a find('tokens') you will get the tokens inside it
    female_placeholder:
        the hashmap for holding the count of pronouns
    refer:
        please refer to annotation in the previous function to understand all  
        about the function.
'''
root = tree.getroot()
for names in femalenames:
    for child in root:
        for docm in child:
            for sents in docm:
#                print sent
                for sent in sents:
                    '''just crossed the sentence and is at the tokens'''
                    name = sent[0][0].text
#                    print name
                    if name == names:
#                        i=0
                        for tokn in sent.findall('token'):
                            for tk in tokn.findall('POS'):
                                if tk.text == 'PRP' or tk.text == 'PRP$':
#                                    i = i + 1
#                                    print tk.text
                                    female_placeholder[names]= female_placeholder[names] + 1
                            
                        
                
print female_placeholder