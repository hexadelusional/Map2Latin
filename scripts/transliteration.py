#!/usr/bin/env python
import sys
import os
import subprocess
import MAP

def transliterate(word, translit_map):
    return ''.join([translit_map.get(ch, ch) for ch in word])

def transliterate_file(input_file, output_file, translit_map):
    with open(input_file, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f]

    latin_words = [transliterate(word, translit_map) for word in words]

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        for word in latin_words:
            f.write(word + '\n')

    print(f"Transliterated {os.path.basename(input_file)} -> {os.path.basename(output_file)}")

# --- CLI ---
if len(sys.argv) != 4:
    print("Usage: python transliteration.py <language_name> <input_file_name> <output_file_name>")
    sys.exit(1)

language_name = sys.argv[1].lower()
input_file_name = sys.argv[2]
output_file_name = sys.argv[3]

# Correct paths from scripts folder
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)

input_file = os.path.join(parent_dir, "originals", input_file_name)
output_file = os.path.join(parent_dir, "translits", output_file_name)

# Special handling for Russian, Ukrainian, Macedonian
special_scripts = {
    "russian": "russianTransliteration.py",
    "ukrainian": "ukrainianTransliteration.py",
    "macedonian": "macedonianTransliteration.py"
}

if language_name in special_scripts:
    script_path = os.path.join(base_dir, special_scripts[language_name])
    subprocess.run(["python", script_path, input_file, output_file])
    print(f"Transliterated {os.path.basename(input_file)} -> {os.path.basename(output_file)}")
    sys.exit(0)

# General transliteration for other languages
try:
    translit_map = getattr(MAP, language_name)
except AttributeError:
    print(f"Error: Map '{language_name}' not found in MAP.")
    sys.exit(1)

transliterate_file(input_file, output_file, translit_map)
