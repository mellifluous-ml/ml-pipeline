"""
dummy cluster
"""
import gensim.downloader
from gensim.models import Word2Vec, KeyedVectors
from gensim.models.word2vec import Text8Corpus
from gensim.similarities.annoy import AnnoyIndexer

from prefect import task, Flow, Parameter


@task(log_stdout=True)
def clustering_place_holder():
    """
    dummy ml
    """
    text8_path = gensim.downloader.load("text8", return_path=True)
    print(text8_path)

    params = {
        'alpha': 0.05,
        'vector_size': 100,
        'window': 5,
        'epochs': 5,
        'min_count': 5,
        'sample': 1e-4,
        'sg': 1,
        'hs': 0,
        'negative': 5,
    }
    model = Word2Vec(Text8Corpus(text8_path), **params)
    wv = model.wv
    print("Using trained model", wv)

    # 100 trees are being used in this example
    annoy_index = AnnoyIndexer(model, 100)
    # Derive the vector for the word "science" in our model
    vector = wv["science"]
    # The instance of AnnoyIndexer we just created is passed
    approximate_neighbors = wv.most_similar([vector], topn=11, indexer=annoy_index)
    # Neatly print the approximate_neighbors and their corresponding cosine similarity values
    print("Approximate Neighbors")
    for neighbor in approximate_neighbors:
        print(neighbor)

    normal_neighbors = wv.most_similar([vector], topn=11)
    print("\nExact Neighbors")
    for neighbor in normal_neighbors:
        print(neighbor)


with Flow("My first flow") as flow:
    # name = Parameter("name")
    clustering_place_holder()


flow.run()
