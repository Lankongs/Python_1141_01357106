import sys

MIRROR = {
    'A': 'A', 'E': '3', '3': 'E', 'J': 'L', 'L': 'J',
    'S': '2', '2': 'S', 'Z': '5', '5': 'Z', '1': '1', '8': '8',
    'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y'
}

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def is_mirrored(s: str) -> bool:

    try:
        mirrored = ''.join(MIRROR[c] for c in reversed(s))
    except KeyError:
        return False 
    return mirrored == s

def classify(s: str) -> str:
    p = is_palindrome(s)
    m = is_mirrored(s)
    if p and m:
        return f"{s} -- is a mirrored palindrome."
    if p:
        return f"{s} -- is a regular palindrome."
    if m:
        return f"{s} -- is a mirrored string."
    return f"{s} -- is not a palindrome."

def main():
    for line in sys.stdin:
        s = line.strip()
        if s == "":
            continue
        print(classify(s))
        print()

if __name__ == "__main__":
    main()
