def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if word == "":
        return False

    if word[low_index] != word[high_index]:
        print("Não é palíndromo")
        return False

    if low_index >= high_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
