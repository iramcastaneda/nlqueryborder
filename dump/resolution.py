from nltk.inference.resolution import clausify
from nltk.sem.logic import Expression
lexpr = Expression.fromstring
print(clausify(lexpr('pais(x0) & exists z3.(exists z2.(poblacion(z3,z2) & exists z1.(poblacion(India,z1) & excede(z2,z1))) & (x0 = z3))')))

print(clausify(lexpr('(pais(x0) & colinda(x0,mar_negro) & capitales(x0,z19))')))
#
#whq(x0,exists z19.(whq(x0,(pais(x0) & colinda(x0,mar_negro) & capitales(x0,z19))) & (x0 = z19)))
