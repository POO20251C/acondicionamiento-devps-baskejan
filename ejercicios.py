#Ejercicio 1

def suma_caract(n):
    #convertir el número a str
    string_num = str(n)
    sum = 0
    for letter in string_num:
        sum = sum + int(letter)
    return sum

#ejercicio 2

def contar_vocales(text):
    cont = 0
    for word in text:
        print(word)
        for letter in word:
            if letter in ["a","e","i", "o", "u", "A", "E", "I", "O", "U"]:
                cont = cont + 1
    return cont


#ejercicio 3

def palindrome(text):
    join_word = ""
    for word in text:
        join_word.join(word)
    if str(join_word) == "".join(reversed(join_word)):
        return "SI"
    else:
        return "NO"    

    
  
#ejercicio 4

def invertir_lista_num(list):
    new_list = []
    idx = len(list) - 1
    while idx >= 0:
        new_list.append(list[idx])
        idx = idx - 1
    return  new_list


                
#ejercicio 5

def contar_pal(text):
    cont = 0
    for word in text.split(" "):
        print(word)
        cont = cont + 1
    return cont    

#ejercicio 6

def encontrar_max_min(list):
    max = list[0]
    min = list[0]
    for i in range(1, len(list)):
        if max < list[i]:
            max = list[i]
        if min > list[i]:
            min = list[i]    

    return [max, min]

print(encontrar_max_min([1,2,3,-4,6,7,9]))