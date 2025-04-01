from nltk.inference.resolution import clausify
from nltk.sem.logic import Expression

__author__ = 'Administrator'
import  nltk.inference.resolution
Expression
lexpr = Expression.fromstring
#qst([_G1382],pais*[_G1382]&colinda*[_G1382,mexico])
#print(clausify(lexpr('exists x.P(x) | Q(x)')))
print(clausify(lexpr('pais(x) & colinda(x,Inglaterra)')))

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP TERMINATOR
NP -> NP1
NP1 -> DET NP2
NP2 -> NOUN preposicion pname
NP2 -> pname
NOUN -> NOUN2
NOUN2 -> attribute
attribute -> 'capital'
pname  -> 'Mexico'
VP -> VP1
VP1 -> verb
verb -> 'es'
preposicion -> 'de'
pname -> 'Ciudad de Mexico'
DET -> 'la'
TERMINATOR -> '?'
""")
sent=['la','capital','de','Mexico','es','la','Ciudad de Mexico','?']
parser = nltk.ChartParser(groucho_grammar)
trees=parser.parse(sent)
for i in trees:
    print(i)
