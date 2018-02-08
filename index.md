# Squeeze more info from texts with Python

Presentation slides are [here](https://docs.google.com/presentation/d/1klBvWJloXl5pwy6zZGuxZcn5lCQqLLNPz2lEPkU9gC4/edit?usp=sharing).

A previous workshop: [Basic Web Scrapin' 101](https://sandbox.idre.ucla.edu/sandbox/basic-web-scrapin-101)

## Other text-analysis tools to consider:
- [Voyant Tools](https://voyant-tools.org/) and its [panoply of plugins](http://voyant-tools.org/docs/#!/guide/tools). Seriously, there are tons of them.
- The compendium of tools at [TAPor3](http://tapor.ca/tools) (Text Analysis Portal) is a bit dated but still worth shopping through
- [Lexos](http://lexos.wheatoncollege.edu/upload)
- [KNIME](https://www.knime.com/knime-analytics-platform) - the best of the "graphical workflow" tools
- [LDA in the browser!](https://mimno.infosci.cornell.edu/jsLDA/)
- [PhiloLogic5](https://github.com/ARTFL-Project/PhiloLogic5) for building and searching (including fuzzy search) large text corpora

## Core text analysis libraries in Python, with links to documentation:
- [nltk](http://www.nltk.org/): Natural Language Toolkit for NLP and more, incl. interface to Stanford CoreNLP
- [scikit-learn](http://scikit-learn.org/) (aka sklearn, learn is for “machine learning”)
- [gensim](https://radimrehurek.com/gensim/): word2vec, doc2vec, also yet more topic modeling
- Deep learning: [TensorFlow](https://www.tensorflow.org/) and [keras](https://keras.io/)

### The SciPy (scipy.org) open-source “ecosystem”:
- [NumPy](http://www.numpy.org/): core numerical processing tools & data structures
- [pandas](https://pandas.pydata.org/): data frame support, for the R converts
- [SciPy](https://docs.scipy.org/doc/scipy/reference/): scientific computing functions, including clustering
- [matplotlib](https://matplotlib.org/) and [matplotlib.pyplot](https://matplotlib.org/api/pyplot_summary.html) (plotting, dataviz)
- Note that [Jupyter/iPython notebooks](https://jupyter-notebook.readthedocs.io/en/stable/) are also from SciPy

## Try Python for yourself!

- Sign up for a free account on [PythonAnywhere](https://www.pythonanywhere.com).
- Or try to run Python in your Windows desktop -- see tips [here](http://docs.python-guide.org/en/latest/starting/install3/win/) about installing modules, setting up the environment.

## Tutorials

- Neal Caren, An introduction to text analysis with Python: [part 1](http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-1/), [part 2](http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-2/), [part 3](http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-3/)
- Arman Akbarian, [Introduction to Text Mining and Natural Language Processing in Python](http://www.akbarian.org/notes/text-mining-nlp-python/)
- Will Gannon, [Your First Text Mining Project with Python in 3 Steps](http://blog.aylien.com/first-text-mining-project-python-3-steps/)
- Brandon Rose, [Document Clustering with Python](http://brandonrose.org/clustering)
- A Jupyter notebook demonstrating [LDA topic modeling with Python](https://nbviewer.jupyter.org/github/jinmanz/machine-learning/blob/master/Topic%20modelling%20-%20Interactive%20visualization%20%26%20topic%20distribution%20visualization%20%28three%20ebooks%20from%20Gutenburg%29.ipynb#topic=0&lambda=1&term=)

## Interesting text-mining data sets

- A [big list](https://archive.ics.uci.edu/ml/datasets.html?&type=text&view=table) from UCI.
- Another [big list](https://data.world/datasets/text-mining) from DataWorld, including [the Simpsons full-text](https://data.world/data-society/the-simpsons-by-the-data) dataset
- Even more data sets from [Kaggle](https://www.kaggle.com/datasets?sortBy=relevance&group=featured&search=text) (used in data science programming competitions), including [a whole lot of song lyrics](https://www.kaggle.com/mousehead/songlyrics)
- [IMDb film reviews](http://ai.stanford.edu/~amaas/data/sentiment/) (selected for extreme positive or negative sentiment)

## Shameless self-promotion

- A [similarity matrix heatmap](http://babylon.library.ucla.edu/~broadwell/adl_sim/simmap.html) of the Archive for Danish Literature, based on the cosine similarity of the TF-IDF weighted 1/2/3-grams in the texts
- A [clustering visualization](http://babylon.library.ucla.edu/~broadwell/corpusmaps/scandinavian/AfDL_similarity_clusters.html) of the same corpus
- A comparison of the [relative Shannon entropies](http://babylon.library.ucla.edu/~broadwell/corpusmaps/scandinavian/AfDL_entropy.html) of the texts across the same corpus
- A combined, interactive TF-IDF weighted 1/2/3-gram cosine similarity (upper left) + LDA topic (lower right) [similarity heatmap](http://babylon.library.ucla.edu/~broadwell/waka/mergedmap.html) for the 21 imperial anthologies of Japanese waka poetry
- Another [combined heatmap](http://etkspace.scandinavian.ucla.edu/~broadwell/etksim/itextmap.html), this one showing both text cosine simlarity (lower right) and detected instances of text reuse (upper left) for the 30,000+ stories in Evald Tang Kristensen's collected Danish folklore
