from uuid import _ifconfig_getnode
import nltk
from nltk.inference.resolution import clausify
import grammautils
from nltk import Expression
from nltk.grammar import CFG,FeatureGrammar

__author__ = 'Administrator'
from nltk import grammar, parse,root_semrep,Tree


#que pais tiene una poblacion que exceda a la poblacion de la India?


g=grammautils.process_gramma(grammautils.get_gramma())
#print(g)
gramma=FeatureGrammar.fromstring(g)
#original="Ciudad de Mexico es la capital de Mexico?"
#original="la capital de Mexico es la Ciudad de Mexico?"
#original="que pais colinda con Inglaterra ?"
#print ("PREGUNTA>"+sentence)
while True:
        #original=input("PREGUNTA:")

        original="cuales son las capitales de que paises que colindan con el Mar Negro"
        sentence=original
        inputs=grammautils.pre_process_sentence(sentence.replace("?"," ?").replace("."," ."))
        trees = grammautils.local_parse(inputs,gramma)
        tree=trees[0]
        print(tree)
        print(root_semrep(tree))
        fullLogic=""
        for i in root_semrep(tree):
            print(i)
            fullLogic+=str(i)
        print("fullLogic is")
        print(fullLogic)
        if(len(trees)>1):
            print("tree has two or more options")
        tree.draw()
        input("nada")

nltk.inference.resolution