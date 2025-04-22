def edit_distance(s1, s2):

    cache = {}

    def calcular(i, j):

        if (i, j) in cache:
            return cache[(i, j)]

        if i == len(s1):
            return len(s2) - j  
        if j == len(s2):
            return len(s1) - i  

        if s1[i] == s2[j]:
            resultado = calcular(i + 1, j + 1)
        else:
            inserir = 1 + calcular(i, j + 1)         
            excluir = 1 + calcular(i + 1, j)         
            substituir = 1 + calcular(i + 1, j + 1)  

            resultado = min(inserir, excluir, substituir)

        cache[(i, j)] = resultado
        return resultado

    return calcular(0, 0)


if __name__ == "__main__":
    print("Distância de Edição (Levenshtein Distance)")
    s1 = input("Digite a primeira string: ").strip()
    s2 = input("Digite a segunda string: ").strip()

    distancia = edit_distance(s1, s2)
    print(f"\nA distância de edição entre '{s1}' e '{s2}' é: {distancia}")