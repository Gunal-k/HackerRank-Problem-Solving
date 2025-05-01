def designerPdfViewer(h, word):
    return max(h[ord(c) - ord('a')] for c in word) * len(word)

if __name__ == '__main__':
    h = list(map(int, input().split()))
    word = input().strip()
    print(designerPdfViewer(h, word))