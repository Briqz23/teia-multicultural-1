def quebrar_string(string):
    lista = [string[i:i+100] for i in range(0, len(string), 100)]
    return lista
texto = "Esta é uma string de exemplo que será quebrada em pedaços de 100 caracteresxemplo que será quebrada em pedaços de 100 caracteresxemplo que será quebrada em pedaços de 100 caracteres."
lista_texto = quebrar_string(texto)
print(lista_texto)
