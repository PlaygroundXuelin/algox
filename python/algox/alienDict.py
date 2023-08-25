def find_pair_order(a: str, b:str):
    for i in range(len(a)):
        x = a[i]
        y = b[i]
        if x == y:
            continue
        return x, y
    return None


def find_order(words: [str]):
    """
    Given a list of words ordered lexically, find order of characters in alien language.

    Analysis:
    For each two words, can figure out 1 pair order by removing common prefix. 
    If a word is proper prefix of the other, no order derived.
    """
    prev = None
    nodes = {}
    chars = set()
    for w in words:
        for c in w:
            chars.add(c)
        if prev is None:
            prev = w
            continue
        pair = find_pair_order(prev, w)
        prev = w
        if pair is None:
            continue
        (x, y) = pair
        if x in nodes:
            nodes[x].add(y)
        else:
            nodes[x] = {y}
    ordered_chars = []
    while len(chars) > 0:
        ch = None
        for c in chars:
            if c in nodes:
                continue
            ch = c
            break
        ordered_chars.append(ch)
        chars.remove(ch)
        orphans = set()
        for k in nodes:
            if c in nodes[k]:
                if len(nodes[k]) == 1:
                    orphans.add(k)
                nodes[k].remove(c)
        for k in orphans:
            nodes.pop(k)
    ordered_chars.reverse()
    return ordered_chars

if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(find_order(words))
