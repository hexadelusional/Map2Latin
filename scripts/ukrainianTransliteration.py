import sys

# --- Map ---
ukrainian_map = {
    'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
    'Г': 'H', 'г': 'h', 'Ґ': 'G', 'ґ': 'g', 'Д': 'D', 'д': 'd',
    'Е': 'E', 'е': 'e', 'Є': 'Ye', 'є': 'ye', 'Ж': 'Zh', 'ж': 'zh',
    'З': 'Z', 'з': 'z', 'И': 'Y', 'и': 'y', 'І': 'I', 'і': 'i',
    'Ї': 'Yi', 'ї': 'yi', 'Й': 'Y', 'й': 'y', 'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh', 'Ц': 'Ts', 'ц': 'ts',
    'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch',
    'Ь': '', 'ь': '', 'Ю': 'Yu', 'ю': 'yu', 'Я': 'Ya', 'я': 'ya',
    'Ы': 'Y', 'ы': 'y',    # Russian letters
    'Ё': 'Yo', 'ё': 'yo',
    'Э': 'E', 'э': 'e'
}

def transliterate(word):
    result = ''
    for i, ch in enumerate(word):
        if ch in ['Є', 'є']:
            result += 'ye' if i == 0 else 'ie'
        elif ch in ['Ї', 'ї']:
            result += 'yi' if i == 0 else 'i'
        elif ch in ['Ю', 'ю']:
            result += 'yu' if i == 0 else 'iu'
        elif ch in ['Я', 'я']:
            result += 'ya' if i == 0 else 'ia'
        else:
            result += ukrainian_map.get(ch, ch)
    return result

# --- CLI ---
if len(sys.argv) != 3:
    print("Usage: python ukrainianTranslit.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f]

latin_words = [transliterate(word) for word in words]

with open(output_file, 'w', encoding='utf-8') as f:
    for word in latin_words:
        f.write(word + '\n')
