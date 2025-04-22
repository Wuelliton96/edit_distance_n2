# Edit Distance com Memoization (Programação Dinâmica)

Este projeto implementa uma solução para o problema de **Edição de Texto (Edit Distance / Levenshtein Distance)** utilizando **recursão com memoization (programação dinâmica)**, conforme exigido na atividade acadêmica.

---

## Descrição do Problema

O problema consiste em calcular o número mínimo de operações necessárias para transformar uma string em outra. As operações permitidas são:

- Inserção de um caractere
- Remoção de um caractere
- Substituição de um caractere

O objetivo é encontrar a menor sequência de operações possível para realizar essa transformação.

---

## Estratégia Utilizada

- **Abordagem**: Recursiva
- **Otimização**: Utilização de memoization para evitar recomputações
- **Estrutura de Cache**: `dict` (hashtable nativa do Python) com acesso em tempo O(1)
- **Melhoria de desempenho**: Subproblemas são armazenados e reutilizados durante a execução

---

## Tecnologias Utilizadas

- Linguagem: **Python 3**
- Não foram utilizadas bibliotecas externas
- Apenas estruturas nativas como `dict` para memoization

---

## Estrutura do Projeto

```
edit_distance/
├── edit_distance.py
└── README.md
```

---

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Execute o arquivo `edit_distance.py` no terminal ou em um ambiente Python:

```bash
python edit_distance.py
```

3. O programa solicitará duas strings como entrada e exibirá a distância de edição entre elas.

---

## Exemplos de Teste

| String 1  | String 2   | Distância Esperada | Justificativa                                 |
|-----------|------------|---------------------|-----------------------------------------------|
| gato      | rato       | 1                   | Substituição de 'g' por 'r'                   |
| casa      | caso       | 1                   | Substituição de 'a' por 'o'                   |
| livro     | livro      | 0                   | Strings iguais                                |
| sapo      | sabão      | 2                   | Substituição + inserção                       |
| a         | abc        | 2                   | Inserção de 'b' e 'c'                         |
| correr    | coruja     | 4                   | Substituições e inserções necessárias         |
| gato      | gatinho    | 4                   | Inserção de 'i', 'n', 'h', 'o'                |

---

## Requisitos da Atividade Atendidos

- [x] Implementação 100% recursiva
- [x] Utilização de memoization com `dict`
- [x] Cache acessado em tempo O(1)
- [x] Verificação no cache antes de cada chamada recursiva
- [x] Código comentado e organizado
- [x] Interação com usuário via `input()`

---

## 👥 Equipe
- Alexandre Tessaro Vieira
- Edson Borges Polucena
- Leonardo Pereira Borges
- Richard Schmitz Riedo 
- Wuelliton Christian dos Santos.
---

## 📘 Licença

Este projeto é apenas para fins acadêmicos.
