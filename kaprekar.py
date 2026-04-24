numero = float(input("Insira um número: ")) #entrada do número
i = 1 #variável para quantidade de iterações
if numero%1 == 0: #verificação se o número é inteiro
    if numero > 0: #verificação se o número é positivo
        if numero <= 9999: #verficação se o número possui somente 4 digitos 
            numero = int(numero) #converte a variável para inteiros
            if numero == 6174:
                print("Parabéns, 6174 é a constante de Kaprekar!!")

            #ciclo de iterações
            while (numero != 6174) and (i <= 7):
                #separação dos digitos da milhar, centena, dezena e unidade
                milhar = numero//1000 
                centena = (numero//100) %10 
                dezena = (numero//10) %10
                unidade = numero%10
                print("[",milhar,"|",centena,"|",dezena,"|",unidade,"]")
                
                #verificação se o número possui no máximo dois digitos iguais
                if (milhar == centena) + (milhar == dezena) + (milhar == unidade) >= 2 or (centena == dezena) + (centena == unidade) >=2 or (dezena == unidade) >=2:
                    print("DADO INVALIDO! Insira um com no máximo dois dígitos iguais") 
                    numero = 6174 

                #Etapa para ordenar os números os digitos maiores
                else: 
                    digito1 = milhar
                    digito2 = centena
                    digito3 = dezena
                    digito4 = unidade

                    #Faz a troca do digito1 para o maior número entre os demais digitos
                    if digito1 > digito2:
                        temp = digito1
                        digito1 = digito2
                        digito2 = temp
                    if digito1 > digito3:
                        temp = digito1
                        digito1 = digito3
                        digito3 = temp
                    if digito1 > digito4:
                        temp = digito1
                        digito1 = digito4
                        digito4 = temp
                    
                    #Faz a troca do digito2 para o maior número entre os digitos restantes
                    if digito2 > digito3:
                        temp = digito2
                        digito2 = digito3
                        digito3 = temp
                    if digito2 > digito4:
                        temp = digito2
                        digito2 = digito4
                        digito4 = temp

                    #Faz a troca dos números restantes
                    if digito3 > digito4:
                        temp = digito3
                        digito3 = digito4
                        digito4 = temp
                    
                    #reconstrução do número em crescente e decrescente
                    NDC = digito1*1000 + digito2*100 + digito3*10 + digito4 #Número em Dígitos Crescentes
                    NDD = digito1 + digito2*10 + digito3*100 + digito4*1000 #Número em Dígitos Decrescentes

                    #Subtração do NDD pelo NDC - Iterações
                    numero = NDD - NDC
                    print("Iteração",i,":",NDD,"-",NDC,"=",numero)
                    i += 1
        else:
            print("DADO INVALIDO! Insira um número com no máximo 4 dígitos")
    elif numero == 0:
        print("DADO INVALIDO! Insira um número diferente de Zero")
    else:
        print("DADO INVALIDO! Insira um número positivo")
else: 
    print("DADO INVALIDO! Insira um número inteiro")