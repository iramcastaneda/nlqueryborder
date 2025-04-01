import re

patten_simplify_dcl="capital\(\w*,\w*\)"
pattern_simplify_swh=""

def is_property(value):
    if(str(value).__contains__("\P.")):
        return True
    return False
def is_quantifier(value):
    if(str(value).__contains__("exists")):
        return True
    return False
def deconvert_properties(value):
    pattern_property="(\\\P\.P\(\w*\))"
    pattenn_word="\(\w*\)"
    for result in re.findall(pattern_property,value):
        for res in re.findall(pattenn_word,result):
            value=value.replace(result,res)
    return value




def local_parse(inputs,gramma):
    from nltk.grammar import FeatureGrammar
    from nltk.parse import FeatureChartParser

    if isinstance(gramma, FeatureGrammar):
        cp = FeatureChartParser(gramma)
    else:
        return ""

    syntrees = list(cp.parse(inputs))
    return syntrees

def get_paises():
    results=""
    with open("data/base_paises","r") as file:
        for i in file:
            results=results+i
    file.close()
    return results

def get_paises_with_sem():
    results=""
    with open("data/paises","r") as file:
        for i in file:
            results=results+i
    file.close()
    return results
def get_ciudades_with_sem():
    results=""
    with open("data/ciudades","r") as file:
        for i in file:
            results=results+i
    file.close()
    return results

def get_gramma():
    gramma=""
    with open("data/gramatica","r", encoding='ISO-8859-1') as file:
            for i in file:
                    print(i)
                    gramma+=i
    return gramma

def process_gramma(gramma):
    gramma=gramma.replace("$PAIS", get_paises_with_sem())
    gramma=gramma.replace("$CIUDADES", get_ciudades_with_sem())

    return gramma

def pre_process_sentence(sentence):
    sentence_cleaned=' '.join(sentence.split())
    list_fixed_tokens="Mar Negro|Ciudad de Mexico|mayor o igual a|mayor o igual que|menor o igual a|menor o igual que|mayor a|mayor que|menor a|menor que|igual a|igual que|distinto de|diferente de|colinda con|colindan con|colinde con|colinden con|de pesos".split("|")
    for fixedtoken in list_fixed_tokens:
        if fixedtoken in sentence_cleaned:
            sentence_cleaned=sentence_cleaned.replace(fixedtoken,fixedtoken.replace(" ","_"))

    sentence_cleaned=sentence_cleaned.split()

    for idx in range(0,len(sentence_cleaned)):
        if "_" in sentence_cleaned[idx]:
            sentence_cleaned[idx]=sentence_cleaned[idx].replace("_"," ")
    return sentence_cleaned


def pre_process_sentence(sentence):
    sentence_cleaned=' '.join(sentence.split())
    list_fixed_tokens="mar negro|ciudad de mexico|mayor o igual a|mayor o igual que|menor o igual a|menor o igual que|mayor a|mayor que|menor a|menor que|igual a|igual que|distinto de|diferente de|colinda con|colindan con|colinde con|colinden con|de pesos".split("|")
    for fixedtoken in list_fixed_tokens:
        if fixedtoken in sentence_cleaned:
            sentence_cleaned=sentence_cleaned.replace(fixedtoken,fixedtoken.replace(" ","_"))

    sentence_cleaned=sentence_cleaned.split()

    for idx in range(0,len(sentence_cleaned)):
        if "_" in sentence_cleaned[idx]:
            sentence_cleaned[idx]=sentence_cleaned[idx].replace("_"," ")
    return sentence_cleaned
def get_grammar_simplify(gramma):
    found=re.findall(gramma,"")
    if(len(found)>0):
        return found[0]
    return ""
def get_type_sentence(typeLabel):
    found=re.findall("'.*'",typeLabel)
    if(len(found))>0:
        return found[0].replace("'","")
def split_into_parenthesis(str):
    list=[]
    count=0
    index=0
    first=True
    for i in str:
        if(count==0):
            list.append(i)
            if(not first):
                index+=1
            first=False
        else:
            list[index]+=i
        if(i =="("):
            count+=1
        if(i==")"):
            count-=1
    return list

def pre_proces_dcl(logic):
    list=split_into_parenthesis(logic)
    pn=""
    if(is_property(list[-1])):
        pn=list.pop()
    else:
        pn=list.pop(0)
    if(is_quantifier(pn)):
        pn=pn[1:len(pn)-1]
        pn=split_into_parenthesis(pn)
        list=[pn[0]]+list
        pn=pn[1]
    logic="".join(list)
    logic=logic.replace("(w)",pn)
    logic=logic.replace("P(x0)","P")
    logic=deconvert_properties(logic)
    return logic

def pre_process_lambda(fullLogic,type):
    if(type in "SDCL"):
        return pre_proces_dcl(fullLogic)
    if(type in "Swh"):
        return fullLogic


def optimize_logic(logic,type):
    if(type=="SDCL"):
        extract=re.findall(patten_simplify_dcl,logic)
        if(len(extract)>0):
            return extract[0]
        return ""
    if(type=="Swh"):
        return logic[7:-2]


def pre_process_clausal( raw_clausal):
    TOKENS="whq(x0,"
    array_clausal=raw_clausal.split(TOKENS)
    clausalSTR=array_clausal[len(array_clausal)-1]
    clausal=""
    clausal=split_into_parenthesis(clausalSTR)[0]
#    print(clausal[1:len(clausal)-1])
    return clausal[1:len(clausal)-1]
pre_process_clausal("whq(x0,exists z19.(whq(x0,(pais(x0) & colinda(x0,mar_negro) & capitales(x0,z19))) & (x0 = z19)))")