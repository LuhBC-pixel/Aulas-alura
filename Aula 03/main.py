from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaOrigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url)

moedaorigem, moedadestino = argumentosUrl.extraiArgumentos()

valor = argumentosUrl.extraiValor()

print(moedadestino, moedaorigem, valor)

print(argumentosUrl)