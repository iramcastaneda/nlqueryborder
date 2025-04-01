import nltk
import sys
from nltk.sem.logic import *
while 1:
    try:
        parse= input('PARSE > ')
        if parse.__contains__("salir"):
            print ("exit parse logic")
            break
        lexpr = Expression.fromstring
        e1 = lexpr(parse)
        print(e1)
        print (e1.simplify())
    except:
        e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % e )
        print ("excepition")




