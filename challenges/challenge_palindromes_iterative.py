def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if word == "":
        return False

    if word[0] != word[-1]:
        print("Não é palíndromo")
        return False

    new_word = word[::-1]
    if word == new_word:
        return True

    return False
