from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "moedaorigem=real&moedadestino=dolar"

argumentosUrl = ExtratorArgumentosUrl(url)

moedaorigem, moedadestino = argumentosUrl.extraiArgumentos()
print(moedadestino, moedaorigem)