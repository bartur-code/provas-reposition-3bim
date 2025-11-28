def maioroumenor(a, b, c, d, e):
    menor = a 
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    if d < menor:
        menor = d
    if d < menor:
        menor = e
    return menor
 

# 5 6 1 9 10   
a = int(input()) 
b = int(input()) 
c = int(input()) 
d = int(input()) 
e = int(input()) 
menor = maioroumenor(a, b, c, d, e)
print(menor)