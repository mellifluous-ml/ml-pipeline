from pathlib import Path
from pprint import pprint
from spacy.lang.en import English


nlp = English()

links_text = Path("data/firefox-history-titles.txt").read_text()
tokens = [
    token_.lemma_.lower() or token_.text.lower()
    for token_ in nlp(links_text)
    if not token_.is_stop and token_.is_alpha
    ]
pprint(tokens)