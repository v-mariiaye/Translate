from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text : str, scr : str, dest : str) -> str:
    try:
        translated_text = GoogleTranslator(source=src, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text : str, set : str) -> str:
    try:
        detected_lang = detect(text)
        if set == "lang":
            return detected_lang
        elif set == "confidence":
            return 1.0
        else:
            return f"Language: {detected_lang}, Confidence: N/A"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    language_code = lang
    language_name = LANGUAGES.get(language_code)
    return f"Назва мови для коду '{language_code}': {language_name}"

def LanguageList(out: str, text: str , limit=11):
    if text:
        translator = GoogleTranslator()

    if out == 'screen':
        print("N Language ISO-639 code Text")
        print("-" * 40)
        count = 1

        for code, language in GoogleTranslator.get_supported_languages(as_dict=True).items():
            if text:
                translation = GoogleTranslator(source='auto', target=code).translate(text)
                print(f"{count} {language} {code} {translation}")
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

            for code, language in GoogleTranslator.get_supported_languages(as_dict=True).items():
                if text:
                    translation = GoogleTranslator(source='auto', target=code).translate(text)
                    file.write(f"{language} {code} {translation}\n")
                else:
                    file.write(f"{code} {language}\n")

                count += 1

                if count >= limit:
                    print("Готово, результат збережено в файлі 'LANGUAGES.txt'")
                    break

    else:
        return "Некоректний формат виводу або відсутній текст"