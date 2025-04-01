import re
stringg='((\P.\Q.exists x0.(P(x0)&Q(x0)))(\P.P(cdexic_saa))))'
pattern="(\\\P\.P\(\w*\))"
results=re.findall(pattern,stringg)
print(stringg)
for result in results:
    for res in re.findall("\(\w*\)",result):
        stringg=stringg.replace(result,res)
