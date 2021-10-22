# Autor: Marcelo Oliveira Almeida
# Email: marcelo.almeida1989@bol.com.br
# esse projeto te como objetivo unificar dois arquivos de dimob
# cada arquivo tem seu propio index iniciando sempre em 1
# para poder unificar corretamente o segundo arquivo precisa iniciar seu index a parti do utimo index no 1º arquivo
# então é isso que o código abaixo faz:
#  abre o aquivo que precisa ser alterado o index, separa ele em listas;
# um lista recebe a parte da string que precisamos alterar e
file = open('dimob.txt')
finalFile = open('final.txt', 'at')

list_of_line = []
list_str1 = []
list_str2 = []
list_one_up = []
for line in file.readlines():
    list_of_line.append(line)
del list_of_line [0:2]
for item in list_of_line:
    str_linha = item
    list_str1.append(str_linha[0:26])
    list_str2.append(str_linha[26:])
i = 436
for l in list_str1:
    str_up = l
    str_replace = str_up[0:23]
    str_up = str_up.replace(str_up, str_replace + str(i))
    list_one_up.append(str_up)
    i = i + 1
l = 0
while l <= len(list_one_up) - 1:
    final_str = str(list_one_up[l] + list_str2[l])
    finalFile.write(final_str)
    l += 1
finalFile.close()
file.close()
