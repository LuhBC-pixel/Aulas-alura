class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("Url inválida!")

    def urlEhValida(self, url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):
        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]
        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) + 1