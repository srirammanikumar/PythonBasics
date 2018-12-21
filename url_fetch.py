"""
module doc strings are placed at the beginning of the file
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """
    Fetch words from URL.
    :param url: the url of doc should be given
    :return: this will return all the strings in the doc
    """
    # the above lines are doc strings which will be returned when you type help(file_name) in REPL after import
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':  # this is for checking if called from shell instead of REPL
    main(sys.argv[1])  # 0th arg is file name
