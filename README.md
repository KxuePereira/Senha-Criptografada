# 🔐 Criptografia RSA do Zero (Python)

Este repositório contém uma implementação acadêmica do **Algoritmo de Criptografia RSA** construído inteiramente do zero em Python, sem o uso de bibliotecas externas de criptografia.

O projeto foi desenvolvido para aplicar os conhecimentos de modelagem matemática por trás de um dos algoritmos de segurança mais famosos e utilizados do mundo.

## 🚀 Como funciona o código?

O script simula um sistema de login simples. Ao conceder o acesso (quando a senha correta é digitada), ele demonstra o poder do algoritmo RSA criptografando e descriptografando a própria senha inserida, ao vivo, no console.

A mágica acontece através dos seguintes passos matemáticos implementados no código:
1. **Geração de Primos:** Sorteia dois números primos aleatórios ($p$ e $q$).
2. **Cálculo da Função Totiente de Euler ($\phi$):** Calcula a quantidade de números coprimos a $N$.
3. **Geração da Chave Pública ($e, n$):** Encontra um número $e$ que seja coprimo da função Totiente.
4. **Geração da Chave Privada ($d$):** Calcula o inverso multiplicativo modular.
5. **Criptografia e Descriptografia:** Aplica a exponenciação modular caractere por caractere baseando-se em seus valores ASCII.

## 💻 Como executar o script

Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.

1. Faça o clone do repositório:
   ```bash
   git clone https://github.com/KxuePereira/Senha-Criptografada.git
   ```
2. Abra o terminal na pasta baixada.
3. Execute o comando:
   ```bash
   python rsa_criptografia.py
   ```
4. Digite a senha de acesso (Dica: `Unip123`).
5. Observe o console exibindo a geração das Chaves (Pública e Privada), a senha transformada em uma matriz de números criptografados, e por fim, a descriptografia voltando ao texto original legível!

## 👨‍💻 Autor
- **Kauê Vitor Pereira Santos** 
- Projeto acadêmico de segurança da informação e matemática aplicada com Python.
