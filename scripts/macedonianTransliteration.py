import sys

# --- Map ---
macedonian_map = {
    'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Ѓ': 'gj', 'ѓ': 'gj',
    'Е': 'E', 'е': 'e', 'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z',
    'Ѕ': 'Dz', 'ѕ': 'dz', 'И': 'I', 'и': 'i', 'Ј': 'J', 'ј': 'j',
    'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l', 'Љ': 'Lj', 'љ': 'lj',
    'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'Њ': 'Nj', 'њ': 'nj',
    'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'Ќ': 'kj', 'ќ': 'kj',
    'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'H', 'х': 'h',
    'Ц': 'Ts', 'ц': 'ts', 'Ч': 'Ch', 'ч': 'ch', 'Џ': 'Dž', 'џ': 'dž',
    'Ш': 'Sh', 'ш': 'sh'
}

def transliterate(word):
    return ''.join([macedonian_map.get(ch, ch) for ch in word])

# --- CLI ---
if len(sys.argv) != 3:
    print("Usage: python macedonianTranslit.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f]

latin_words = [transliterate(word) for word in words]

with open(output_file, 'w', encoding='utf-8') as f:
    for word in latin_words:
        f.write(word + '\n')
