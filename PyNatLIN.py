from uuid import _ifconfig_getnode
import nltk
from nltk.inference.resolution import clausify
import grammautils
from nltk import Expression
from nltk.grammar import CFG,FeatureGrammar

from nltk import grammar, parse,root_semrep,Tree

#principal flujo


#obtiene la gramatica que esta en archivo data/gramatica
g=grammautils.process_gramma(grammautils.get_gramma())
#creas la gramatica
gramma=FeatureGrammar.fromstring(g)
while True:
    try:
        #obtienes la pregunta
        original=input("PREGUNTA:")
        sentence=original
        sentence=sentence.lower()
        #separa los tokens especiales
        inputs=grammautils.pre_process_sentence(sentence.replace("?"," ?").replace("."," ."))
        #print(inputs)
        trees = grammautils.local_parse(inputs,gramma)

        nltk.treetransforms
        if (len(trees)>0):
             tree=trees[0]
             type=grammautils.get_type_sentence(str(trees[0][0].label()).split("\n")[0])
             #print(tree)
             fullLogic=""
             try:
                for subLog in root_semrep(trees[0]):
                #print(subLog)
                    fullLogic+=subLog
             except:
                 fullLogic="".join(root_semrep(tree[0]))

             lexpr = Expression.fromstring
             exp=lexpr(fullLogic)
             print("Logica completa:")
             print(fullLogic)
             print("Logica simplificada")
             print(exp.simplify())
             print("Forma clausal:")
             clausalStr=str(exp.simplify())
             lexpr = Expression.fromstring
             print(clausify(lexpr(grammautils.pre_process_clausal(clausalStr))))
    except Exception as e:
        print(e)
        print("Lo siento no entendi la pregunta :"+original)
        pass