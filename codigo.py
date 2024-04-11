import random

def primos(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
           return False
        i += 6
    return True

def totient(numero): 
    if(primos(numero)):
        return numero - 1
    else:
        return False
    
def gerar_num(num): 
    def mdc(n1,n2):
        resto = 1
        while(n2 != 0):
            resto = n1 % n2
            n1 = n2
            n2 = resto
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e

def gerar_primos(): 
    while True:
        x = random.randrange(1,100) 
        if(primos(x)==True):
            return x
        
def mod(a,b):
    if(a<b):
        return a
    else:
        c = a % b
        return c

def criptografar(letras,e,n):
    tamanho = len(letras)
    i = 0
    lista = []
    while(i < tamanho):
        let = letras[i]
        k = ord(let)
        k = k**e
        d = mod(k,n)
        lista.append(d)
        i += 1
    return lista

def descriptografar(cripto,n,d):
    lista = []
    i = 0
    tamanho = len(cripto)
    while i < tamanho:
        resultado = cripto[i]**d
        texto = mod(resultado,n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista

def chave_priv(total,e):
    d = 0
    while(mod(d * e,total) != 1):
        d += 1
    return d

texto = input("Digite a senha: ")
senha = "Unip123"

while (texto != senha):
    print("Acesso Negado!")
    texto = input("\nDigite a senha: ")

if (texto == senha):
    p = gerar_primos()
    q = gerar_primos()
    n = p*q 
    y = totient(p)
    x = totient(q)
    totient_N = x * y 
    e = gerar_num(totient_N)
    chave_publica = (n, e)

    print('\nACESSO PERMITIDO!')
    print('\nChave Pública:', chave_publica)
    d = chave_priv(totient_N,e)
    print('Chave Privada:', d, n)
    texto_cripto = criptografar(texto,e,n)
    print('\nMensagem Criptografada:', texto_cripto)
    texto_original = descriptografar(texto_cripto,n,d)
    print('Mensagem Descriptografada:', texto_original)