from googletrans import translator
translator_1=translator()
print("Введите текст для перевода")
translate=input()
text_t=translator_1.translate(translate,src='ru',dest='en')

print("Перевод:",text_t.text)