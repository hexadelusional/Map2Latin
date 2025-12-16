import sys

# --- Map ---
russian_map = {
    'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e',
    'Ё': 'Yo', 'ё': 'yo', 'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z',
    'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh', 'Ц': 'Ts', 'ц': 'ts',
    'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch',
    'Ъ': "", 'ъ': "", 'Ы': 'Y', 'ы': 'y', 'Ь': "", 'ь': "",
    'Э': 'E', 'э': 'e', 'Ю': 'Yu', 'ю': 'yu', 'Я': 'Ya', 'я': 'ya'
}

def transliterate(word):
    result = ''
    for i, ch in enumerate(word):
        if ch in ['Е', 'е']:
            if i == 0 or word[i-1] in 'АаЕеЁёИиОоУуЫыЭэЮюЯяЬьЪъ':
                result += 'ye'
            else:
                result += russian_map[ch]
        else:
            result += russian_map.get(ch, ch)
    return result

# --- CLI ---
if len(sys.argv) != 3:
    print("Usage: python russianTranslit.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f]

latin_words = [transliterate(word) for word in words]

with open(output_file, 'w', encoding='utf-8') as f:
    for word in latin_words:
        f.write(word + '\n')
