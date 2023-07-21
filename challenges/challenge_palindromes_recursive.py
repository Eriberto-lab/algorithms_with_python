def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if word == "":
        return False

    if word[low_index] != word[high_index]:
        print("Não é palíndromo")
        return False

    new_word = word[::-1]
    if word == new_word:
        return True

    return False
