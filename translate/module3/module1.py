from googletrans import Translator, LANGUAGES

def TransLate(text : str, src : str, dest : str) -> str:
    translator = Translator()
    try:

        src_lang = LANGUAGES.get(src, src)
        dest_lang = LANGUAGES.get(dest, dest)
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str) -> str:
    translator = Translator()
    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return str(detected.confidence)
        else:
            return f"Language: {detected.lang}, Confidence: {detected.confidence}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    elif lang in LANGUAGES.values():
        return next(key for key, value in LANGUAGES.items() if value == lang)
    else:
        return "Language not found"

def LanguageList(out: str, text: str = None, limit=11) -> str:

    if text:
        translator = Translator()

    if out == 'screen':
        print("N Language ISO-639 code Text")
        print("-" * 40)
        count = 1

        for code, language in LANGUAGES.items():
            if text:
                translation = translator.translate(text, dest=code)
                print(f"{count} {language} {code} {translation.text}")
            else:
                print(f"{count} {language} {code}")

            count += 1

            if count >= limit:
                break

        print("Ok")

    elif out == 'txt' and text:
        filename = "LANGUAGES.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Language ISO-639 code Text\n" + "-" * 40 + "\n")
            count = 1

            for code, language in LANGUAGES.items():
                if text:
                    translation = translator.translate(text, dest=code)
                    file.write(f"{language} {code} {translation.text}\n")
                else:
                    file.write(f"{code} {language}\n")

                count += 1

                if count >= limit:
                    print("Готово, результат збережено в файлі 'LANGUAGES.txt'")
                    break

    else:
        return "Некоректний формат виводу або відсутній текст"