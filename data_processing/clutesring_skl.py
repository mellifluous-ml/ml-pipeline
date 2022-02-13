from pathlib import Path
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split


links_filepath = Path("./data/links.txt")
links_text = links_filepath.read_text()
links = links_text.splitlines()
words = np.array(links_text.split())

training_set, testing_set = train_test_split(links, test_size=0.3)

X_train_counts = CountVectorizer().fit_transform(words)
X_train_tfidf = TfidfTransformer().fit_transform(X_train_counts)

# X_test_counts = CountVectorizer().fit_transform(testing_set)
# X_test_tfidf = TfidfTransformer().fit_transform(X_test_counts)


model = LogisticRegression()
model.fit(X_train_tfidf, training_set)

# testing_set = np.array(testing_set, dtype=str).reshape(-1, 1)

predictions = model.predict(testing_set)


from pprint import pprint

pprint(predictions)