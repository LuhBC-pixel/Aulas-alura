from cpf_cnpj import Documento
from validate_docbr import CNPJ

cpf_um = 15316264754
#print(cpf_um)

#exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11111111112"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(cpf_um)
print(documento)