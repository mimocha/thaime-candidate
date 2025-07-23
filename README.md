# Thai IME Candidate Selection Engine

This repository contains the Python implementation for a Thai Input Method Editor (IME) candidate selection algorithm.

## Algorithm

The core algorithm for candidate selection will likely be a [Trie](https://en.wikipedia.org/wiki/Trie).
This is a commonly used algorithm for autocorrect and spell checking; it is very fast and fairly memory efficient data structure for selecting word candidates while typing.

The Trie will be used for converting Latin character sequences into potential Thai word candidates. Sequences of Latin characters will form the Trie's edges, and the candidate Thai words forms the nodes.

Candidates will primarily be ranked based on term frequency; with additional ranking criteria (such as word context) to be added later.

### Potential Research Topics:

**Radix Trie / Patricia Trie**

Naive Trie implementation can be memory inefficient. More advanced Trie implementations can provide better space efficiency.

**Context-Aware Candidate Selection**

Using context information, such as recently selected words, to inform what the next words should be.
This can be a standard N-gram based prediction

**Soundex / Metaphone based matching**

A Trie relies on exact spelling matches, whereas common Thai-Latin transliteration (karaoke spelling) is not standardized.
Different people will type out the same Thai word in different Latin spelling, which can cause a naive Trie to fail.

Adding a system that attempts phonetic-based matching of Latin input with plausible Thai output could allow for more lenient / fuzzy matching.

## Datasets

Thai NLP datasets are used to generate word frequency data,
and subsequently, the [Trie](https://en.wikipedia.org/wiki/Trie) structure for candidate selection.
Having a representative Thai word frequency data is vital for returning good candidate selections.

The selected corpus includes:
- Formal writing
- Informal writing
- Name-entities

We will balance out the contributions of each dataset by calculating the term frequency for each corpus separately,
dividing the term frequency for each word by the corpus size,
then combining the final proportions together in a weighted sum.
This will prevent the candidate selection algorithm from being biased towards the largest corpus,
while maintaining the benefits of using large corpus.

Datasets were selected from these compiled lists of datasets:
- (github/PyThaiNLP/classification-benchmarks)[https://github.com/PyThaiNLP/classification-benchmarks]
- (github/keyreply/Thai-NLP-Dataset)[https://github.com/keyreply/Thai-NLP-Dataset]
- (NLP for Thai NER)[https://nlpforthai.com/tasks/ner/]

Source | Description | Link
-------|-------------|-----
Prachathai | Prachathai 67K news article corpus - formal news article | [github/PyThaiNLP/prachathai-67k](https://github.com/PyThaiNLP/prachathai-67k)
Wisesight | Wisesight sentiment corpus - informal, social media text | [github/PyThaiNLP/wisesight-sentiment](https://github.com/PyThaiNLP/wisesight-sentiment) 
Wongnai | Wongnai corpus - informal internet review | [github/wongnai/wongnai-corpus](https://github.com/wongnai/wongnai-corpus)
Thai Wikipedia | Wikipedia articles in Thai - formal, 1.5GB XML | [Wikimedia.org](https://dumps.wikimedia.org/thwiki/latest/thwiki-latest-pages-articles.xml.bz2)
HSE Thai Corpus | 50 million tokens downloaded from websites, mostly news site. | [web-corpora.net](http://web-corpora.net/ThaiCorpus) or [github](https://github.com/nevmenandr/thai-language)