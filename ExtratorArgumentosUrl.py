class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!")

    def urlEhValida(self, url):
        if url and url.startswith('https://bytebank.com'):
            return True
        else:
            return False

    def extraiArgumentos(self):
        buscaMoedaOrigem = "moedaorigem".lower()
        buscaMoedaDestino = "moedadestino".lower()

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoeadaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        moedaDestino = self.url[indiceInicialMoedaDestino: indiceFinalMoedaDestino]
        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    def trocaMoeadaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor=".lower()
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor