"""

anagram_finder.py

    Description: find and print to screen all anagrams in a dictionary with at least four letters and at least as many
     anagrams as letters

    Instructions: An anagram is a word formed by rearranging the letters of another, like "topside" and "deposit". In
    some cases, there might be as many (or more) anagrams than there are characters, like "post", "spot", "stop" and
    "tops".

    Write a program to find all of the anagrams in a dictionary in which there are at least 4 letters in the word and
    at least as many anagrams as there are letters.

    The dictionary will be a file on disk with one line per word. Your operating system likely already has such a file
    in /usr/dict/words or /usr/share/dict/words.

    The output produced by your code should be in this format:

    emit, item, mite, time
    merit, miter, mitre, remit, timer
    reins, resin, rinse, risen, serin, siren
    inert, inter, niter, retin, trine
    inset, neist, snite, stein, stine, tsine

"""
__author__ = 'Drew Smith'
__email__ = 'ajsmith007@gmail.com'

import sys
import collections
import logging

logging.basicConfig(filename='anagram_finder.log', level=logging.INFO)


def normalize(word):
    """
    Normalize the word by removing spaces and converting to all lowercase ordered string
    :param word: string
    :return: normalized string
    """
    word = word.strip().lower()
    return ''.join(sorted(word))


def find_anagrams(word_file='/usr/share/dict/words'):
    """
    Find anagrams in a set of words from a file on disk
    :param word_file: default: '/usr/share/dict/words'
    :return: dict of words from the word file that are anagrams
    """
    logging.info('Running find_anagrams with word_file: %s' % word_file)
    anagram_dict = collections.defaultdict(list)
    try:
        with open(word_file) as words:
            for word in words:
                anagram_dict[normalize(word)].append(word.strip().lower())
            return anagram_dict
    except Exception as e:
        logging.error(repr(e))
        raise e


def output_anagrams(anagram_dict, min_length=4):
    """
    Display anagrams to console
    :param anagram_dict:
    :return: None. print to stdout
    """
    logging.info('Running output_anagrams with min_length: %s' % min_length)
    counter = 0
    for k, v in anagram_dict.items():
        if len(set(v)) >= len(k) >= min_length:
            counter += 1
            print(', '.join(set(v)))
    logging.info('Found %s anagrams' % counter)

if __name__ == "__main__":
    import datetime
    logging.info('====================================================================================================')
    start_time = datetime.datetime.now()
    logging.info('Staring anagram_finder.py at: %s' % start_time)
    logging.info('====================================================================================================')

    if len(sys.argv) > 2:
        sys.stderr.write('Usage: python anagram_finder.py <dictionary of words>')
        sys.exit(1)
    elif len(sys.argv) == 1:
        anagrams = find_anagrams()
    else:
        anagrams = find_anagrams(sys.argv[1])
    output_anagrams(anagrams)

    logging.info('====================================================================================================')
    end_time = datetime.datetime.now()
    logging.info('Completed anagram_finder.py at: %s (Execution time: %s)' % (end_time, end_time - start_time))
    logging.info('====================================================================================================')

