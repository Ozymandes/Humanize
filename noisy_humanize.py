#!/usr/bin/env python3
"""
noisy_humanize.py  –  add human fingerprints without changing meaning
Usage:
    python noisy_humanize.py Draft.txt          # creates Draft_clean.txt
Options:
    --keep-original  (always leaves Draft.txt untouched)
    --seed N         (reproducible output)
"""

import argparse, pathlib, random, re, sys, unicodedata
from math import ceil

# ------------------------------------------------------------------
# 1.  reversible low-signal edits
# ------------------------------------------------------------------
TYPO_ODDS = 0.015          # ~1.5 % of words get a typo
CONTRACT_ODDS = 0.18       # 18 % of eligible phrases
FILLER_ODDS = 0.06         # 6 % of sentences start with filler
HEDGE_EVERY = 300          # words
STARTER_LIST = ["And", "But", "So", "Actually", "Honestly", "Anyway"]
PERSONAL_ASIDES = ["I think", "I believe", "in my view", "personally", "I mean"]

# typo map – only common words, 1-char slip
TYPO_MAP = {
    "the": ("teh", "hte"), "and": ("adn", "annd"), "to": ("too",),
    "people": ("poeple",), "because": ("becuase",), "definitely": ("definately",),
    "probably": ("prolly",), "going": ("gonna",), "want": ("wanna",),
    "got": ("gotta",), "about": ("abotu",), "could": ("cuold",),
}

CONTRACTIONS = {
    "it is": "it's", "you are": "you're", "they are": "they're",
    "we are": "we're", "I am": "I'm", "do not": "don't", "does not": "doesn't",
    "is not": "isn't", "are not": "aren't", "was not": "wasn't",
    "were not": "weren't", "will not": "won't", "cannot": "can't",
    "could not": "couldn't", "would not": "wouldn't", "should not": "shouldn't",
    "have not": "haven't", "has not": "hasn't", "had not": "hadn't",
    "did not": "didn't",
}

# ------------------------------------------------------------------
# 2.  helpers
# ------------------------------------------------------------------
def rng_choice(rng, seq):
    return seq[rng.randint(0, len(seq) - 1)]

def add_typos(words, rng):
    """1-char slip, keeps capitalisation."""
    out = []
    for w in words:
        lw = w.lower()
        if lw in TYPO_MAP and rng.random() < TYPO_ODDS:
            typo = rng_choice(rng, TYPO_MAP[lw])
            if w[0].isupper():
                typo = typo.capitalize()
            out.append(typo)
        else:
            out.append(w)
    return out

def add_contractions(text, rng):
    for long, short in CONTRACTIONS.items():
        if rng.random() < CONTRACT_ODDS:
            text = re.sub(r'\b' + long + r'\b', short, text, flags=re.I, count=1)
    return text

def add_sentence_stuff(sentence, rng, word_counter):
    """filler starter + occasional hedge."""
    s = sentence.strip()
    if not s:
        return s
    # filler starter
    if rng.random() < FILLER_ODDS:
        s = rng_choice(rng, STARTER_LIST) + ', ' + s[0].lower() + s[1:]
    # personal aside every ~HEDGE_EVERY words
    if word_counter % HEDGE_EVERY < 10 and rng.random() < 0.5:
        aside = rng_choice(rng, PERSONAL_ASIDES)
        s = aside + ', ' + s[0].lower() + s[1:]
    return s

def jitter_length(sents, rng):
    """merge or split to break uniform cadence."""
    out = []
    i = 0
    while i < len(sents):
        if rng.random() < 0.15 and i + 1 < len(sents):  # merge two short
            out.append(sents[i] + ' ' + sents[i + 1])
            i += 2
        else:
            out.append(sents[i])
            i += 1
    # occasionally split long
    final = []
    for s in out:
        if len(s) > 140 and rng.random() < 0.20:
            mid = len(s) // 2
            # split at nearest space
            split_at = s.rfind(' ', mid - 10, mid + 10)
            if split_at > 0:
                final.extend([s[:split_at], s[split_at + 1:]])
            else:
                final.append(s)
        else:
            final.append(s)
    return final

# ------------------------------------------------------------------
# 3.  core
# ------------------------------------------------------------------
def noisy_humanize(text: str, seed=None, intensity='intermediate') -> str:
    rng = random.Random(seed)

    # Adjust odds based on intensity
    intensity_multipliers = {
        'beginner': 0.5,      # Less humanizing
        'intermediate': 1.0,  # Normal humanizing
        'advanced': 2.0       # More humanizing
    }
    multiplier = intensity_multipliers.get(intensity, 1.0)

    # 1. byte-level clean
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Cf')  # strip format controls
    text = unicodedata.normalize('NFKC', text)

    paragraphs = re.split(r'(\n\s*\n)', text)
    out_paras = []
    word_counter = 0

    # Global typo odds
    global_typo_odds = TYPO_ODDS * multiplier
    global_contract_odds = min(CONTRACT_ODDS * multiplier, 0.5)
    global_filler_odds = min(FILLER_ODDS * multiplier, 0.15)

    for para in paragraphs:
        if re.match(r'\n\s*\n', para):
            out_paras.append(para)
            continue
        # split sentences
        sents = re.split(r'(?<=[.!?])\s+', para.strip())
        sents = jitter_length(sents, rng)
        new_sents = []
        for sent in sents:
            words = re.findall(r"\b\w+\b|[^\w\s]", sent)  # keep punctuation tokens
            # count real words
            word_counter += len([w for w in words if w.isalpha()])
            words = add_typos_with_odds(words, rng, global_typo_odds)
            sent = ' '.join(words)
            sent = add_sentence_stuff_with_odds(sent, rng, word_counter, global_filler_odds)
            new_sents.append(sent)
        para = ' '.join(new_sents)
        para = add_contractions_with_odds(para, rng, global_contract_odds)
        out_paras.append(para)

    # Clean up spacing issues before returning
    result = ''.join(out_paras)
    result = clean_spacing(result)
    return result

def add_typos_with_odds(words, rng, typo_odds):
    """1-char slip, keeps capitalisation."""
    out = []
    for w in words:
        lw = w.lower()
        if lw in TYPO_MAP and rng.random() < typo_odds:
            typo = rng_choice(rng, TYPO_MAP[lw])
            if w[0].isupper():
                typo = typo.capitalize()
            out.append(typo)
        else:
            out.append(w)
    return out

def add_contractions_with_odds(text, rng, contract_odds):
    for long, short in CONTRACTIONS.items():
        if rng.random() < contract_odds:
            text = re.sub(r'\b' + long + r'\b', short, text, flags=re.I, count=1)
    return text

def add_sentence_stuff_with_odds(sentence, rng, word_counter, filler_odds):
    """filler starter + occasional hedge."""
    s = sentence.strip()
    if not s:
        return s
    # filler starter
    if rng.random() < filler_odds:
        s = rng_choice(rng, STARTER_LIST) + ', ' + s[0].lower() + s[1:]
    # personal aside every ~HEDGE_EVERY words
    if word_counter % HEDGE_EVERY < 10 and rng.random() < 0.5:
        aside = rng_choice(rng, PERSONAL_ASIDES)
        s = aside + ', ' + s[0].lower() + s[1:]
    return s

def clean_spacing(text: str) -> str:
    """Clean up all spacing issues"""
    # Remove extra spaces between words
    text = re.sub(r' {2,}', ' ', text)
    # Remove spaces before punctuation
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)
    # Fix spacing after punctuation (ensure space)
    text = re.sub(r'([.!?])([a-zA-Z])', r'\1 \2', text)
    # Remove trailing spaces before newlines
    text = re.sub(r' +\n', '\n', text)
    # Remove spaces at start/end
    text = text.strip()
    return text

def clean_humanized_text(text: str) -> str:
    """Remove filler words, personal asides, and fix spacing issues from humanizer"""
    # Remove sentence starters at the beginning
    starters_pattern = r'^(And|But|So|Actually|Honestly|Anyway|Well|Now|Basically|Literally),?\s+'
    text = re.sub(starters_pattern, '', text, flags=re.IGNORECASE | re.MULTILINE)

    # Remove personal asides (case insensitive)
    asides = [
        r'\bi think\b,?\s*',
        r'\bi believe\b,?\s*',
        r'\bin my view\b,?\s*',
        r'\bpersonally\b,?\s*',
        r'\bi mean\b,?\s*',
        r'\bto me\b,?\s*',
        r'\bas far as i\'?m concerned\b,?\s*',
        r'\bfrom my perspective\b,?\s*',
    ]
    for aside in asides:
        text = re.sub(aside, '', text, flags=re.IGNORECASE)

    # Fix capitalization after removing starters
    text = re.sub(r'^([a-z])', lambda m: m.group(1).upper(), text, flags=re.MULTILINE)
    text = re.sub(r'([.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)

    # Clean up ALL whitespace issues
    # Remove extra spaces between words
    text = re.sub(r' {2,}', ' ', text)
    # Remove spaces before punctuation
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)
    # Fix spacing after punctuation
    text = re.sub(r'([.!?])([a-zA-Z])', r'\1 \2', text)
    # Remove spaces at start/end of lines
    text = re.sub(r'^\s+|\s+$', '', text, flags=re.MULTILINE)
    # Fix multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove trailing spaces before newlines
    text = re.sub(r' +\n', '\n', text)

    text = text.strip()

    return text

# ------------------------------------------------------------------
# 4.  CLI
# ------------------------------------------------------------------
def parse_args():
    p = argparse.ArgumentParser(description='Add human fingerprints without changing meaning')
    p.add_argument('file', type=pathlib.Path, help='text to clean')
    p.add_argument('-o', '--out', type=pathlib.Path, help='output file (default: <name>_clean.txt)')
    p.add_argument('--seed', type=int, help='reproducible random')
    return p.parse_args()

def main():
    args = parse_args()
    src = args.file
    if not src.exists():
        sys.exit(f'error: {src} not found')
    original = src.read_text(encoding='utf-8')
    cleaned = noisy_humanize(original, seed=args.seed)

    dest = args.out or src.with_name(src.stem + '_clean.txt')
    dest.write_text(cleaned, encoding='utf-8')
    print(f'Noisy humanise complete -> {dest}  (original untouched)')

if __name__ == '__main__':
    main()
