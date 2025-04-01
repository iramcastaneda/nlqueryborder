from uuid import _ifconfig_getnode
import nltk
from nltk.inference.resolution import clausify
import grammautils
from nltk import Expression
from nltk.grammar import CFG,FeatureGrammar
from nltk.draw import draw_trees
__author__ = 'Administrator'
from nltk import grammar, parse,root_semrep,Tree


#que pais tiene una poblacion que exceda a la poblacion de la India?
def get_gramma():
    gramma=""
    with open("data/gramatica2","r") as file:
            for i in file:
                    gramma+=i
    return gramma

g=grammautils.process_gramma(get_gramma())
print(g)
gramma=FeatureGrammar.fromstring(g)
original="Raul regala a Roberto un gato"
#original="la capital de Mexico es la Ciudad de Mexico?"
#original="que pais colinda con Mexico ?"
#print ("PREGUNTA>"+sentence)

while True:
    #original=input("PREGUNTA:")
    input("PREGUNTA:")
    sentence=original
    inputs=grammautils.pre_process_sentence(sentence.replace("?"," ?").replace("."," ."))
    trees = grammautils.local_parse(inputs,gramma)
    if (len(trees)>0):
        tree=trees[0]
        for i in tree:
            print(i)
        print("".join(root_semrep(tree)))
        tree.draw()




