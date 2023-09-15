from textblob import TextBlob


class AnalizadorDeSentimiento:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"


analizador = AnalizadorDeSentimiento()
resultado = analizador.analizar_sentimiento("The ")
print(resultado)