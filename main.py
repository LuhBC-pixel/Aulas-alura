# PRIMEIRA PARTE
# cpf = 15626987913
# cpf = str(cpf)
# tamanho_cpf = len(cpf)
# print(tamanho_cpf)

# SEGUNDA PARTE
from cpf import Cpf

# cpf = 15626987913

# objeto_cpf = Cpf(cpf)

# TERCEIRA PARTE
# cpf = "15616987913"
#objeto_cpf = Cpf(cpf)

# fatia_um = cpf[:3]
# fatia_dois = cpf[3:6]
# fatia_tres = cpf[6:9]
# fatia_quatro = cpf[9:]
# print(fatia_um)
# print(fatia_dois)
# print(fatia_tres)
# print(fatia_quatro)

# QUARTA PARTE
# cpf = "15616987913"
#objeto_cpf = Cpf(cpf)

# fatia_um = cpf[:3]
# fatia_dois = cpf[3:6]
# fatia_tres = cpf[6:9]
# fatia_quatro = cpf[9:]

# cpf_formatado = f"{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}"

# print(cpf_formatado)

# QUINTA PARTE

# cpf= "15398745687"
# objeto_cpf = Cpf(cpf)

# print(objeto_cpf)

# SEXTA PARTE
from validate_docbr import CPF

cpf = CPF()

print(cpf.validate("012.345.678-90"))
print(cpf.validate("111.111.111-11"))