# BIPBOP
# -*- coding: utf-8 -*-

# Autor: Humberto Diogenes

import re


def validate_cpf(cpf):
    """Check CPF is valid. If it is not, return None."""
    cpf = ''.join(re.findall(r'\d+', cpf))
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return
    cpf_numbers = list(map(int, cpf))
    multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(9, 11):
        remainder = sum([a * b for a, b in zip(cpf_numbers[:i], multipliers)]) * 10 % 11
        digit = 0 if remainder == 10 else remainder
        if digit != cpf_numbers[i]:
            return
        multipliers.insert(0, 11)
    return cpf


def validate_cnpj(cnpj):
    """Check CNPJ is valid. If it is not, return None."""
    cnpj = ''.join(re.findall(r'\d+', cnpj))
    if len(cnpj) != 14:
        return
    cnpj_numbers = list(map(int, cnpj))
    multipliers = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(12, 14):
        remainder = sum([a * b for a, b in zip(cnpj_numbers[:i], multipliers)]) % 11
        digit = 0 if remainder < 2 else 11 - remainder
        if digit != cnpj_numbers[i]:
            return
        multipliers.insert(0, 6)
    return cnpj
