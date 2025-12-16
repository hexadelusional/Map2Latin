# Map2Latin
Map2Latin is a command-line tool that transliterates Eurocontrol Member States languages to Latin script using dictionary-based mappings.

## Features
- Handles special transliteration rules for specific languages.
- Works directly from the command line without any GUI.
- Automatically organizes input and output files.

## Project Structure

Map2Latin/
├─ originals/ # Place your original text files here
├─ translits/ # Output transliterated files are saved here
├─ scripts/ # Python scripts for transliteration
│ ├─ transliteration.py # Main script
│ ├─ MAP.py # Dictionary mappings to Latin for every language
│ ├─ russianTransliteration.py # Special rules proper to Russian cyrillic
│ ├─ ukrainianTransliteration.py # Special rules proper to Ukrainian cyrillic
│ ├─ macedonianTransliteration.py # Special rules proper to Madeconian cyrillic

## Usage

```bash
python scripts/transliteration.py <language_name> <input_file> <output_file>
```

## Example
python scripts/transliteration.py russian russian.txt russianT.txt

## Supported Languages

Albanian, Armenian, Bosnian, Bulgarian, Croatian, Czech, Danish, Dutch, Esperanto, Estonian, Finnish, French, Georgian, German, Greek, Hebrew, Hungarian, Icelandic, Italian, Latvian, Lithuanian, Macedonian, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swedish, Turkish, Ukrainian.

## Notes

All input files go in originals/ and output files are saved in translits/.

Russian, Ukrainian, and Macedonian have special transliteration rules handled by separate scripts.

Add new languages by updating MAP.py and writing a custom transliteration function if needed.