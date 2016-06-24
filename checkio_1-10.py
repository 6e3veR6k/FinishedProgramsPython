# 1	=============================================================================
def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    new_phrase = ",".join(list(phrases))
    new_str = new_phrase.replace("right", "left")
    return new_str


# 2	=============================================================================
def multiply_digits(number):
    return int(reduce(lambda x, y: int(x)*int(y), str(number).replace("0", '')))


# 3	=============================================================================
def count_words(text, words):
    count = 0
    for word in words:
        if word in text.lower():
            count += 1
    return count


# 4	=============================================================================
def diff_max_min(*args):
	return max(args) - min(args) if args else 0


# 5	=============================================================================
def find_message(text):
    """Find a secret message"""
    return "".join([letter for word in text.split() for letter in word if letter.isupper()])


# 6	=============================================================================
def index_power(array, n):
    return array[n]**n if 0 <= n < len(array) else -1


# 7	=============================================================================
def foo(array):
    return sum(array[::2])*array[-1] if array else 0

# 8	=============================================================================
def find_message(text):
    x = [letter for letter in text if letter.isupper()]     
    return "".join(x)


# 9 =============================================================================
def count_inversion(seq):
    count = 0
    for i in range(len(seq)):
        for j in range(len(seq[:i])):
            if seq[i] < seq[j]:
                count += 1
    return count


def count_inversion(sequence):        
    return sum(x > y for l, x in enumerate(sequence) for y in sequence[l:])


def count_inversion(sequence):
    sequence = list(sequence)
    count = 0
    while sequence != sorted(sequence):
        for i in range(len(sequence) - 1):
            if sequence[i] > sequence[i+1]:
                count += 1
                temp = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = temp
    return count


# 10 =============================================================================
def end_of_other(word_set):
    for base_word in word_set:
        for ends_word in word_set-{base_word}:
            if base_word.endswith(ends_word):
                return True
    return False

print end_of_other({"hello", "lo", "he"})