 from ExtratorArgumentosUrl import ExtratorArgumentosUrl

# url = "moedaorigem=real&moedadestino=dolar"

# argumentosUrl = ExtratorArgumentosUrl(url)

# moedaorigem, moedadestino = argumentosUrl.extraiArgumentos()
# print(moedadestino, moedaorigem)

url ='https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150'
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)
# Aqui ta tudo bem, teste agora o caso em que “moedaorigem=moedadestino”.
url ='https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150'
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)