from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "moedaorigem=real&moedadestino=dolar"

argumentosUrl = ExtratorArgumentosUrl(url)

moedaorigem, moedadestino = argumentosUrl.extraiArgumentos()

valor = argumentosUrl.extraiValor()

print(moedadestino, moedaorigem, valor)

print(argumentosUrl)