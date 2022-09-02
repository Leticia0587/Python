from datetime import datetime


medida = float(input("Digite uma distância em metros"))
cm = medida *100
mm = medida *1000
km = medida /1000
hm = medida /100
dam = medida/10
dm = medida*10

print("A medida de {}m corresponde a \n{}cm \n{}mm, \n{}km, \n{}hm, \n{}dam, \n{}dm".format(medida,cm,mm,km,hm,dam,dm))
