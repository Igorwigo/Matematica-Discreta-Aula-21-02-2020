import math



d1="They say: Oh my God, I see the way you shine Take your hand, my dear, and place them both in mine You know you stopped me dead when I was passing by And now I beg to see you dance just one more time Ooh, I see you, see you, see you every time"
#dance Monkey


d2="No início foi assim Terminou tá terminado Cada um pro seu lado Não precisa ligar maisv"#Liberdade Provisória

d3="Olha a cabeleira do Zezé Será que ele é? Será que ele é?"#cabeleira do seu zeze

d4="Você pensa que cachaça é água? Cachaça não é água não Cachaça vem do alambique E água vem do ribeirão"#cachaça não é água


#bag of words
bow_d1=d1.split(" ")

bow_d2=d2.split(" ")

bow_d3=d3.split(" ")

bow_d4=d4.split(" ")
#Total de palavras
# print(len(bow_d1)+len(bow_d2)+len(bow_d3)+len(bow_d4))
#-----------------------------------------------------------------------------------

unique_words = set(bow_d1).union(set(bow_d2)).union(set(bow_d3)).union(set(bow_d4))

#print(unique_words)

#contando quantas vezes a palavra se repete em cada documento(d)
tc_d1 = dict.fromkeys(unique_words,0)
for w in bow_d1:
    tc_d1[w]+=1

tc_d2= dict.fromkeys(unique_words,0)
for w in bow_d2:
    tc_d2[w]+=1

tc_d3=dict.fromkeys(unique_words,0)
for w in bow_d3:
    tc_d3[w]+=1


tc_d4=dict.fromkeys(unique_words,0)
for w in bow_d4:
    tc_d4[w]+=1


#print(tc_d1)


#Frequencia do termo
tf_d1={}
total=float(len(bow_d1))
for w,c in tc_d1.items():
    tf_d1[w] = c / total


tf_d2={}
total=float(len(bow_d2))
for w,c in tc_d2.items():
    tf_d2[w] = c / total


tf_d3={}
total=float(len(bow_d3))
for w,c in tc_d3.items():
    tf_d2[w] = c / total


tf_d4={}
total=float(len(bow_d4))
for w,c in tc_d4.items():
    tf_d2[w] = c / total





documents=[tc_d1,tc_d2,tc_d3,tc_d4]
n=len(documents)
idf=dict.fromkeys(unique_words,0)
for d in documents:
    for w, c in d.items():
        if c > 0:
            idf[w]+=1
for w, c in idf.items():
    idf[w] = math.log(n/float(c))




#TF-IDE(Multiplicação)

tf_idf_d1={}
for w, c in tf_d1.items():
    tf_idf_d1[w] = c * idf[w]

tf_idf_d2={}
for w, c in tf_d2.items():
    tf_idf_d2[w] = c * idf[w]

tf_idf_d3={}
for w, c in tf_d3.items():
    tf_idf_d3[w] = c * idf[w]

tf_idf_d4={}
for w, c in tf_d4.items():
    tf_idf_d4[w] = c * idf[w]


#Distância entre documentos
#Distância entre d1 e d2

ds=[]
for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d2[w]
    ds.append(dif * dif)
soma1=0
for i in ds:
    soma1 +=1
#------------------------------------

for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d3[w]
    ds.append(dif * dif)
soma2=0
for i in ds:
    soma2 +=1
#------------------------------------

for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d4[w]
    ds.append(dif * dif)
soma3=0
for i in ds:
    soma3 +=1
#------------------------------------

for w in unique_words:
    dif = tf_idf_d2[w] - tf_idf_d3[w]
    ds.append(dif * dif)
soma4=0
for i in ds:
    soma4 +=1
#------------------------------------

for w in unique_words:
    dif = tf_idf_d2[w] - tf_idf_d4[w]
    ds.append(dif * dif)
soma5=0
for i in ds:
    soma5 +=1
#------------------------------------

for w in unique_words:
    dif = tf_idf_d3[w] - tf_idf_d4[w]
    ds.append(dif * dif)
soma6 =0
for i in ds:
    soma6 +=1
#------------------------------------



    
dist_d1_d2 = math.sqrt(soma1)
dist_d1_d3 = math.sqrt(soma2)
dist_d1_d4 = math.sqrt(soma3)
dist_d2_d3 = math.sqrt(soma4)
dist_d2_d4 = math.sqrt(soma5)
dist_d3_d4 = math.sqrt(soma6)




print(dist_d1_d2)
print(dist_d1_d3)
print(dist_d1_d4)
print(dist_d2_d3)
print(dist_d2_d4)
print(dist_d3_d4)

























