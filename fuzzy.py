# A fuzzy grep implementation using n-grams and list/set comprehension

def ngrams(text, n=3):
    text = text.lower()
    indices = range(len(text) - n + 1)
    return {text[i:i + n] for i in indices}


def match(qgrams, text):
    matches = ngrams(text) & qgrams
    return len(matches) / len(qgrams)


def find(query, filepath, cf=0.6):
    q = ngrams(query)
    with open(filepath) as lines:
        matches = [(m, l) for l in lines if (m := match(q, l)) > cf]
        return sorted(matches, reverse=True)


if __name__ == "__main__":
    while True:
        query = input('\nfind: ')
        if len(query) < 3:
            break
        print('-' * 50)
        for cf, line in find(query, 'fuzzy.py'):
            print('%.2f : %s ' % (cf, line.strip()))

