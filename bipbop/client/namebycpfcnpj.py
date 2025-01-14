# BIPBOP
# -*- coding: utf-8 -*-

from bipbop.client.cpfcnpj import validate_cpf, validate_cnpj
from bipbop.client.exception import Exception
from bipbop.client.webservice import WebService


class NameByCPFCNPJ:
    def evaluate(cpfcnpj, birthday, apikey=None):
        if validate_cpf(cpfcnpj):
            if birthday is None:
                raise Exception("É necessário a data de nascimento para consultar um CPF.")
        elif validate_cnpj(cpfcnpj):
            pass
        else:
            raise Exception("O documento informado não é um CPF ou CNPJ válido.")

        ws = WebService(apikey)
        return ws.post("SELECT FROM 'BIPBOPJS'.'CPFCNPJ'",
                       {
                           'documento': cpfcnpj,
                           'nascimento': birthday
                       }).find("./body/nome").text

    evaluate = staticmethod(evaluate)
