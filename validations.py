import re

def valida_nome(nome):
    nomespace = nome.replace(' ', '')
    if nomespace.isalpha() and len(nome) <= 100:
        return True
    else:
        return False

def valida_cpf(cpf):
    if re.match("^[0-9\-]+$", cpf):
        cpf = cpf.replace('-', '')
    if re.match("^[0-9\.]+$", cpf):
        cpf = cpf.replace('.', '')
    if len(cpf) == 11:
        return True
    else:
        return False

def formata_cpf(cpf):
    cpf = re.sub('[^\d]', '', cpf)
    return cpf

def valida_data(nascimento):
    if re.match("^[0-9\/]+$", nascimento):
        if  len(nascimento) <= 10 and  len(nascimento) >= 8:
            return True
    return False

def valida_numero(num):
    pattern = r'^[0-9.]+$'
    if (re.match(pattern, num)):
        return True
    
    return False

def valida_inteiro(num):
    num = int(num)
    if type(num) is int:
        return True
    return False
