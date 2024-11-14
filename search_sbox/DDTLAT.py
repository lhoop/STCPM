import numpy as np


def differential_uniformity(sbox):
    n = len(sbox)
    m = int(np.log2(n))
    max_diff_count = 0

    diff_table = np.zeros((n, n), dtype=int)

    for alpha in range(1, n):
        for x in range(n):
            y_diff = sbox[x] ^ sbox[x ^ alpha]
            diff_table[alpha][y_diff] += 1

    max_diff_count = np.max(diff_table[1:])
    return max_diff_count, diff_table

def linearity(sbox):
    n = len(sbox)
    m = int(np.log2(n))

    input_masks = range(1, n)
    output_masks = range(1, n)

    max_bias = 0

    for input_mask in input_masks:
        for output_mask in output_masks:
            bias = 0
            for x in range(n):
                input_parity = bin(x & input_mask).count('1') % 2
                output_parity = bin(sbox[x] & output_mask).count('1') % 2
                if input_parity == output_parity:
                    bias += 1
            bias = abs(bias - n // 2)
            max_bias = max(max_bias, bias)

    linearity_value = 2 * max_bias
    return linearity_value


def number_to_truth_table(num, n_bits):
    truth_table = [(num >> i) & 1 for i in range(2**n_bits)]
    return truth_table

def boolean_function_linearity_from_number(num, n_bits):
    #n_bits = int(np.log2(num.bit_length()))
    truth_table = number_to_truth_table(num, n_bits)
    max_bias = 0

    for input_mask in range(1, 2**n_bits):
        bias = 0
        for x in range(2**n_bits):
            input_parity = bin(x & input_mask).count('1') % 2

            output = truth_table[x]

            if input_parity == output:
                bias += 1

        bias = abs(bias - len(truth_table) // 2)
        max_bias = max(max_bias, bias)
    

    linearity_value = 2 * max_bias
    return linearity_value


def algebraic_degree(num, n_bits):
    truth_table = number_to_truth_table(num, n_bits)
    n = n_bits
    anf = truth_table.copy()
    

    for i in range(2**n):
        for j in range(i):
            if i & j == j:
                anf[i] ^= anf[j]

    degree = 0
    for i in range(2**n):
        if anf[i] != 0:
            degree = max(degree, bin(i).count('1'))
    
    return degree
