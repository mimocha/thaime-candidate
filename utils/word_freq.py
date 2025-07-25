import re
from collections import Counter

from tqdm import tqdm
from pythainlp.tokenize import word_tokenize

def text_cleaning(input_text: str, keep_num: bool = False) -> str:
    """Simple text preprocessing function to remove all non-Thai characters"""

    # Keep Thai characters (https://th.wikipedia.org/wiki/Thai_(บล็อกยูนิโคด))
    if keep_num is True:
        pattern = r'([^\u0E01-\u0E3A\u0E40-\u0E4E.\d\u0E50-\u0E59,])'
    else:
        pattern = r'([^\u0E01-\u0E3A\u0E40-\u0E4E.])'
    text = re.sub(pattern, r' ', input_text)

    # Replace Arabic & Thai numbers with a special token
    if keep_num is True:
        text = re.sub(r'[\d\u0E50-\u0E59][\d\u0E50-\u0E59.,]*', '<NUM>', text)

    # Collapse multiple consequtive whitespace characters into a single space
    text = re.sub(r'\s+', ' ', text)

    return text

def text_tokenize(input_text: str, engine='newmm') -> list[str]:
    """Tokenize Thai string with PyThaiNLP.word_tokenize function"""
    return word_tokenize(input_text, engine=engine, keep_whitespace=False)

def text_count(input_list: list[str]) -> Counter:
    """Use collections.Counter to count tokens"""
    return Counter(input_list)

def filter_token_counter(input_counter: Counter, min_freq: int = 3) -> Counter:
    """Filter out non-words, special tokens, and low frequency words"""

    filtered_counter = Counter()
    for word, freq in tqdm(input_counter.items()):
        # Keep only tokens with valid Thai characters
        if re.search(r'[\u0E01-\u0E3A\u0E40-\u0E4E]', word) is None:
            continue

        # For string with only 1 unique character (i.e. repeated character string like 'aaaaaaaa')
        # Truncate to 1 character
        if len(set(word)) == 1:
            word = word[0]

        # For 1 character string, if it is just a lone vowel or special character (i.e. ฯ )
        # Don't add it to counter (because we cannot transliterate them)
        if (len(word) == 1) and re.search(r'[\u0E2F-\u0E4F]', word):
            continue

        # Add valid word to count
        filtered_counter[word] += freq

    # Filter by minimum number of counts
    if min_freq > 0:
        removal_list = list()
        for word, freq in filtered_counter.items():
            if freq < min_freq:
                removal_list.append(word)
        for word in removal_list:
            _ = filtered_counter.pop(word)

    return filtered_counter

def normalize_frequency(input_counter: Counter) -> dict:
    """Normalize the word frequency value by dividing by the total number of words in the corpus"""

    word_frequency = dict()
    total_counts = input_counter.total()
    for word, counts in tqdm(input_counter.items()):
        word_frequency[word] = counts / total_counts

    return word_frequency

