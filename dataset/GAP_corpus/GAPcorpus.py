# https://convokit.cornell.edu/documentation/gap.html
from convokit import Corpus, download
gap_corpus = Corpus(filename=download("gap-corpus"))
print(gap_corpus)