### 1) 
Observe o trecho de código abaixo:
```
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça
    {   
        K = K + 1;   
        SOMA = SOMA + K;  
    }

imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA?

Resposta: O valor da variável SOMA será 91.

### 2) 
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.     IMPORTANTE:   Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 

Resposta: Vide arquivo `main.py`.

### 3) 
Descubra a lógica e complete o próximo elemento:     
```
a) 1, 3, 5, 7, ___   
b) 2, 4, 8, 16, 32, 64, ____   
c) 0, 1, 4, 9, 16, 25, 36, ____   
d) 4, 16, 36, 64, ____   
e) 1, 1, 2, 3, 5, 8, ____   
f) 2, 10, 12, 16, 17, 18, 19, ____ 
```

Resposta: 
```
a) 1, 3, 5, 7, 9 (adicionar 2 ao número anterior)   
b) 2, 4, 8, 16, 32, 64, 128 (multiplicar o número anterior por 2)   
c) 0, 1, 4, 9, 16, 25, 36, 49 (elevar ao quadrado os números 0, 1, 2, 3, 4, 5, 6, 7)   
d) 4, 16, 36, 64, 100 (elevar ao quadrado os números pares 2, 4, 6, 8, 10)   
e) 1, 1, 2, 3, 5, 8, 13 (sequência Fibonacci)   
f) 2, 10, 12, 16, 17, 18, 19, 200 (números que começam com a letra D) 
```