from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

translator = Translator()

fraseEN = "The food was disgusting. The filet was very raw and the salad was hot ?? I can not believe how rude the waiter was. I will not return to this site"
fraseES = "La comida estaba asquerosa. El filete estaba muy crudo y la ensalada estaba caliente?? No puedo creer lo grosero que era el camarero. No volveré a este sitio"
fraseAT = "tozi restorant e mnogo losh"

blobEN = TextBlob(fraseEN)
blobES = TextBlob(fraseES)

print("Frase en inglés: ", blobEN.sentiment)
print("Frase en español: ", blobES.sentiment)

traduccion = translator.translate(fraseAT)

fraseTraducida = traduccion.text

blobEStoEN = TextBlob(fraseTraducida)

sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(fraseEN)
print("Analisis VADER")
for k in sorted(ss):
    print('{0}: {1}, '.format(k, ss[k]), end='')
print("")

print("Frase traducida:{}.Sentimiento:{}".format(fraseTraducida, blobEStoEN.sentiment))
