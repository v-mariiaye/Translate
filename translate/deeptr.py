from module3.module2 import *

def main():
    text = "Hello, this is a test."
    target_language = "uk"
    translated_text = translate_text(text, target_language)
    print(f"Переклад на українську: {translated_text}")

def translate_text(text, target_language):
    try:
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    main()
