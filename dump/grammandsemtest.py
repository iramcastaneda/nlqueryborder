from __future__ import print_function
import nltk
from nltk import grammar, parse,root_semrep
g = """
 % start DP
 DP[AGR=?a,SEM=(?d+'&'+?semN)] -> D[AGR=?a,SEM=?d] N[AGR=?n,SEM=?semN]
 D[AGR=[NUM='sg', PERS=3],SEM='P(x)'] -> 'esta' | 'esa' | 'este'
 D[AGR=[NUM='pl', PERS=3]] -> 'estas' | 'esos' | 'estos'
 D[AGR=[NUM='pl', PERS=1]] -> 'nosotros'
 D[AGR=[PERS=2]] -> 'ustedes'
 N[AGR=[NUM='sg', GND='m'],SEM='P(y)'] -> 'chico'
 N[AGR=[NUM='pl', GND='m']] -> 'chicos'
 N[AGR=[NUM='sg', GND='f']] -> 'chica'
 N[AGR=[NUM='pl', GND='f']] -> 'chicas'
 N[AGR=[NUM='sg']] -> 'estudiante'
 N[AGR=[NUM='pl']] -> 'estudiantes'
 """
grammar = grammar.FeatureGrammar.fromstring(g)
tokens = 'este chico'.split()
parser = parse.FeatureEarleyChartParser(grammar)
trees = parser.parse(tokens)
for tree in trees:
    print(tree)

    print("sem is"+str(root_semrep(tree)))