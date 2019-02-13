def search4vowels(phrase: str) -> str:
    """This will search for vowels within a phrase."""
    return set('aeiou').union(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> str:
    """This return set of 'letters' found in the phrase"""
    return set(letters).intersection(set(phrase))
