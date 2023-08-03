# Descrição dos Algoritmos Desenvolvidos

A seguir, descrevo cada um dos algoritmos desenvolvidos para resolver os problemas propostos:

## 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

Neste problema, o objetivo era determinar o horário com a maior quantidade de pessoas estudantes acessando a plataforma. Foi utilizado um algoritmo de busca linear (força bruta) para percorrer a lista de períodos de permanência dos estudantes. Para cada horário, contei quantos estudantes estavam presentes no sistema naquele momento. O horário com o maior número de estudantes foi retornado como o melhor horário para disponibilizar os materiais de estudo. A complexidade desse algoritmo é O(n), onde "n" é o número de períodos de permanência.

## 2 - Criptografia de inversões (Testes)

Neste requisito, foi solicitado a implementação dos testes para uma função de criptografia chamada `encrypt_message`. Os testes garantem que a função de criptografia respeite uma lógica específica. Foram criados diversos casos de teste para validar o funcionamento correto da função `encrypt_message`.

## 3 - Palíndromos (Recursividade)

Neste problema, a função `is_palindrome_recursive` foi desenvolvida para determinar se uma palavra é um palíndromo ou não. Utilizei uma abordagem recursiva para comparar o primeiro caractere com o último, o segundo com o penúltimo, e assim por diante. Caso todos os pares de caracteres correspondentes sejam iguais, a palavra é um palíndromo e a função retorna True. Caso contrário, retorna False. A complexidade desse algoritmo é O(n), onde "n" é o tamanho da palavra.

## 4 - Anagramas (Algoritmo de ordenação)

Para resolver o problema de anagramas, criei a função `are_anagrams`, que recebe duas strings como parâmetro. Utilizei o algoritmo de ordenação rápida (QuickSort) para ordenar as letras das palavras em ordem alfabética. Em seguida, comparei se as palavras ordenadas são iguais, o que indica que são anagramas entre si. A complexidade desse algoritmo depende do algoritmo de ordenação utilizado, sendo O(n log n) no caso do QuickSort.

## 5 - Encontrando números repetidos (Algoritmo de busca)

Para encontrar um número duplicado em uma lista de números inteiros, criei a função `find_duplicate` que recebe uma lista chamada `nums` como parâmetro. Utilizei um algoritmo de busca linear com o auxílio de um dicionário para rastrear os números já encontrados. O algoritmo percorre a lista uma única vez, armazenando os números em um dicionário e, ao encontrar um número repetido, o retorna. A complexidade desse algoritmo é O(n), onde "n" é o número de elementos na lista.

## 6 - Palíndromos (Iteratividade)

Resolvi novamente o problema de palíndromos utilizando uma abordagem iterativa na função `is_palindrome_iterative`. O algoritmo percorre metade da palavra, comparando o caractere correspondente à esquerda com o caractere correspondente à direita. Caso todos os pares de caracteres correspondentes sejam iguais, a palavra é um palíndromo e a função retorna True. Caso contrário, retorna False. A complexidade desse algoritmo é O(n/2), que é aproximadamente O(n) no pior caso.

Esses foram os algoritmos desenvolvidos neste projeto, buscando sempre a melhor complexidade em Big O para garantir soluções eficientes para cada problema.
