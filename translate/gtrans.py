from module3.module1 import *

def main():
    text_to_translate = "Привіт, яка сьогодні погода?"

    translator = Translator()

    translated_text = TransLate(text_to_translate, 'uk', 'en')
    print(f"Переклад з української на англійську: {translated_text}")


    detected_language = LangDetect(text_to_translate, 'translate')
    print(f"Мова тексту: {detected_language}")


    language_code = CodeLang('English')
    print(f"Код мови для 'English': {language_code}")


    result = LanguageList("screen", "Довіра")
    if result == 'Ok':
        print("Операція виконана успішно")
    else:
        print(f"Помилка: {result}")

if __name__ == '__main__':
    main()