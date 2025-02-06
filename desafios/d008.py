m = float(input('Digite o valor em metros: '))
km = m*0.001
hm = m*0.01
dam = m*0.1
m = m
dm = m*10
cm = m*100
mm = m*1000
print('\nEm quilômetros: {}km \nEm hectâmetro: {}hm \nEm decâmetro: {}dam \nEm metros: {}m \nEm decímetros: {}dm \nEm centímetros: {}cm \nEm milímetros: {}mm'.format(km,hm,dam,m,dm,cm,mm))