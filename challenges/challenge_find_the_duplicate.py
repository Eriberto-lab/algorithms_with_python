def find_duplicate(nums=None):
    #  - Retorne False se a função não receber nenhum parâmetro;
    if nums is None:
        return False

    #  - Retorne False se a função receber como parâmetro uma string;
    if isinstance(nums, str):
        return False

    # - Retorne False se a função receber como parâmetro uma lista sem números repetidos;
    if len(set(nums)) == len(nums):
        return False

    #  - Retorne False se a função receber como parâmetro apenas um valor;
    if isinstance(nums, (int, float)):
        return False

    # - Retorne False se a função receber como parâmetro um número negativo;
    if any(num < 0 for num in nums):
        return False

    # - Retorne o número repetivo se a função receber como parâmetro uma lista com números repetidos;
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            return num
        nums_dict[num] = 1

    return False
