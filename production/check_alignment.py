"""Check a word alignment file against the source; cannot verify audio timing."""
import argparse
import json
import math
import re
import unicodedata
from pathlib import Path


def tokens(text):
    return re.findall(r"[^\W_]+(?:['’][^\W_]+)*", unicodedata.normalize('NFC', text), re.UNICODE)


def normalize(word):
    # Turkish dotted I must be lowered before generic casefold.
    return unicodedata.normalize('NFC', word.replace('İ', 'i').replace('I', 'ı').casefold())


def check(text, words, duration):
    errors = []
    expected = tokens(text)
    if not isinstance(words, list):
        return ['words must be a list']
    if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not math.isfinite(duration) or duration <= 0:
        return ['invalid audio duration']
    if len(expected) != len(words):
        errors.append(f'word count: expected {len(expected)}, got {len(words)}')
    prev = 0.0
    for index, item in enumerate(words):
        if not isinstance(item, dict):
            errors.append(f'{index + 1}: invalid entry')
            continue
        word = item.get('word')
        if not isinstance(word, str) or len(tokens(word)) != 1:
            errors.append(f'{index + 1}: invalid word')
        elif index < len(expected) and normalize(tokens(word)[0]) != normalize(expected[index]):
            errors.append(f'{index + 1}: unexpected word {word!r}; expected {expected[index]!r}')
        start, end = item.get('start'), item.get('end')
        if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) for x in (start, end)):
            errors.append(f'{index + 1}: missing or invalid timestamp')
            continue
        if start < prev or end <= start or end > duration:
            errors.append(f'{index + 1}: overlapping, reversed or out-of-range timestamp')
        prev = end
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reference', type=Path, help='Exact spoken script as UTF-8 text')
    parser.add_argument('alignment', type=Path, help='JSON {duration, words:[{word,start,end}]}')
    args = parser.parse_args()
    data = json.loads(args.alignment.read_text(encoding='utf-8'))
    errors = check(args.reference.read_text(encoding='utf-8'), data.get('words'), data.get('duration'))
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print('Structural checks passed; listening and timing review are still required.')


if __name__ == '__main__':
    main()
