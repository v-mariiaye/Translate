import json
from deep_translator import GoogleTranslator


def read_config(config_file):
    with open(config_file, "r") as file:
        config = json.load(file)
    return config


def translate_text(text_file, config_file):
    config = read_config(config_file)

    with open(text_file, "r", encoding="utf-8") as infile:
        text_to_translate = infile.read()

    translated_text = GoogleTranslator(source="auto", target=config['target_language']).translate(text_to_translate)

    with open("translated_text.txt", "w", encoding="utf-8") as outfile:
        outfile.write(translated_text)


if __name__ == "__main__":
    text_file = "text.txt"
    config_file = "config.json"

    translate_text(text_file, config_file)
