# Map2Latin
Map2Latin is a command-line tool that transliterates Eurocontrol Member States languages to Latin script using dictionary-based mappings.

## Features
- Handles special transliteration rules for specific languages.
- Works directly from the command line without any GUI.
- Automatically organizes input and output files.

## Project Structure

```bash
Map2Latin/
├─ originals/ # Original text files here (input)
├─ translits/ # Transliteration files here (output)
├─ scripts/ # Contains all scripts for transliteration
│ ├─ transliteration.py # Main script
│ ├─ MAP.py # Dictionary mappings to Latin
│ ├─ russianTransliteration.py # Special rules proper to Russian cyrillic
│ ├─ ukrainianTransliteration.py # Special rules proper to Ukrainian cyrillic
│ ├─ macedonianTransliteration.py # Special rules proper to Madeconian cyrillic
```

## Usage

```bash
python scripts/transliteration.py <language_name> <input_file> <output_file>
```

## Example

```bash
python scripts/transliteration.py russian russian.txt russianT.txt
```

## Supported Languages

Albanian, Armenian, Bosnian, Bulgarian, Croatian, Czech, Danish, Dutch, Esperanto, Estonian, Finnish, French, Georgian, German, Greek, Hebrew, Hungarian, Icelandic, Italian, Latvian, Lithuanian, Macedonian, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swedish, Turkish, Ukrainian.

## Others

All input files go in originals/ and output files are saved in translits/.

Russian, Ukrainian, and Macedonian have special transliteration rules handled by separate scripts.

Add new languages by updating MAP.py and writing a custom transliteration function if needed.

Most dictionnaries were adapted from [HermitDave's FrequencyWords repository](https://github.com/hermitdave/FrequencyWords) and cleaned for consistency.
