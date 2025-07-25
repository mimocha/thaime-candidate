import re
from collections import Counter

from pythainlp.tokenize import word_tokenize

def text_cleaning(input_text: str, keep_num: bool = False) -> str:
    """Simple text preprocessing function to remove all non-Thai characters"""

    # Keep Thai characters (https://th.wikipedia.org/wiki/Thai_(บล็อกยูนิโคด))
    if keep_num is True:
        pattern = r'([^\u0E01-\u0E3A\u0E40-\u0E4E\u0E50-\u0E59.,0-9])'
    else:
        pattern = r'([^\u0E01-\u0E3A\u0E40-\u0E4E\u0E50-\u0E59.])'
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
