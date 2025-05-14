#exercissio 1- soma de dois numeros:
n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
soma = n1 + n2
print(soma)

#exercissio 2- subtração  de dois numeros:

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
subtracao = n1 - n2
print(subtracao)

#exercissio 3- Multiplicação de dois numeros
n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
multiplicacao = n1 * n2
print(multiplicacao)

#exercissio 4- divisão de dois numeros:

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
divisao = n1/n2
print(divisao)

#exercissio 5- resto de divisão

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
resto =n1 % n2
print(resto)

#exercissio 6- potencia de um numero

n1 = int(input('Informe o numero: '))
n2 = int(input('Informe o expoente: '))
potencia= n1 ** n2

#exercissio 7-media de tres numeros

n1 = float(input('Informe o primeiro numero: '))
n2 = float(input('Informe o seundo numero: '))
n3= float(input('Informe o terceiro numero: '))
media = (n1+ n2+n3)/3
print(media)

#exercissio 8- converssor de temperatura

n1 = float(input('Informe a temperatura: '))
temp = (n1/5) * 9 + 32
print(temp)

#exercissio 9-converção de moeda

n1 = float(input('Informe o valor que quer converter de reais para dolar: R$ '))
conv = n1 * 0,18
print(conv)

#exercissio 10- araea de um retangula

c = float(input('Informe o comprimento: '))
l = float(input('Informe a largura: '))
area= c*l
print(area)

#exercissio 11- perimetro do quadrado

l = float(input('Informe o lado do quadrado: '))
perimetro = l *  4
print(l)

#exercissio 12- area de um triangulo
n1 = float(input('Informe a base do triangulo:  '))
n2 = float(input('Informe a altura do triangulo: '))
area = (n1 * n2 )/2
print(area)

#exercissio 13-area de um circulo

n1 = float(input('Informe o raio do circulo: '))
area = (n1 ** 2) * 3,14
print(area)

#exercissio 14- converssão de metros pra centimetros
n1 = int(input('Informe o metro que deseja converter: '))
cent = n1 * 100
print(cent)

#exercissio 15-horas trabalhadas 

n1 = int(input('Quantas horas vpcê trabalhou: '))
n2 = float(input('Quanto vale a hora: R$'))
sal = n1*n2
print(sal)

#exercissio 16- preço edesconto

n1 = float(input('Informe o valor do produto: '))
n2 = float(input('Informe o percentual de desconto: '))
preco = n1 -(n1 * (n2/100))
print(preco)

#exercissio 17- velocidade media

n1 = float(input('Informe a distancia percorrida em km: '))
n2 = float(input('Informe o tempo gasto em horas: '))
velo = n1/n2
print(velo)

#exercissio 18- converte idade

n1 = int(input('Informe a sua idade: '))
dias = n1 * 365
print(dias)

#exercissio 19- segundo no dia
s = 24 * 60 *60
print(s)

#exercissio 20- imc

n1 = float(input('Informe o peso em kg: '))
n2 = float(input('Informe a altura em metros: '))
imc =  n1/(n2 ** 2)
print(imc)

#exercissio 21- diferença de dois numeros:

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
dif = n1 - n2
if dif < 0:
    dif *= -1
print(dif)

#exercissio 22- divisão inteira

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
div = n1 // n2
print(div)

#exercissio 23-valor absoluto

n1 = float(input('Informe um numero: '))
n1 = int(n1)
print(n1)

#exercissio 24-converte km/h pra m/s
n1 = float(input('Informe a velocidade em km/h: '))
velo = n1 / 3.6
print(velo)

#exercissio 25- formula de baskara

a= int(input('Informe o coeficiente a: '))
b = int(input('Informe o coeficiente b: '))
c = int(input('Informe o coeficiente c: '))
bask1 = (-b +((b**2) - 4 * a *c)**1/2)/2*a
bask2 = (-b -((b**2) - 4 * a *c)**1/2)/2*a
print(f'x1={bask1}|x2={bask2}')

#exercissio 26-valor total de uma compra

a= float(input('Informe o peço do produto 1: '))
b = float(input('Informe o preço do produto 2: '))
c = float(input('Informe o preço do produto 3: '))
total = a+b+c
print(total)

#exercissio 27- converte dias para semana

a= int(input('Informe a quantidade de dias: '))
cont=0
while a > 7:
    a=a - 7
    cont += 1
print(f"{cont} semanas e {a} dias")

#exercissio 28- desconto

a = float(input('Informe o preço do produto: R$ '))
if a > 100:
    if a > 500:
        p = a  - (a*0.10)
    else:
        p = a  - (a*0.05)
print(p)

#exercissio 29-divisão limitada

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o seundo numero: '))
divisao = n1/n2
d = '{:.2f}'.format(divisao)
print(d)
