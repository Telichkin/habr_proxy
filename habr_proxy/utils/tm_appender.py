import re
from itertools import chain


class TMAppender:
    TM = "™"

    def __init__(self, special_len):
        self.special_len = special_len

    def get_modified_text(self, raw_text):
        only_words_regexp = re.compile("[a-zA-Zа-яА-Я'™-]+", re.UNICODE)
        other_symbols = only_words_regexp.split(raw_text)
        raw_words = only_words_regexp.findall(raw_text)
        modified_words = []
        for raw_word in raw_words:
            modified_word = raw_word
            if len(raw_word) == self.special_len:
                modified_word = raw_word + self.TM
            modified_words.append(modified_word)
        modified_words.append("")

        modified_text = ''.join(chain.from_iterable(zip(other_symbols, modified_words)))
        return modified_text
