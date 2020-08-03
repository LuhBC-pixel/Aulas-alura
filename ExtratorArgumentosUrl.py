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
        indiceInicialMoedaDestino = self.url.find("=", 15) + 1

        indiceInicialMoedaOrigem = self.url.find("=") + 1
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]
        return moedaOrigem, moedaDestino