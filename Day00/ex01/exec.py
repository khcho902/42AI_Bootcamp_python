import sys

sentence = sys.argv
del sentence[0]
sentence = " ".join(sentence).swapcase()
print(sentence[::-1])

