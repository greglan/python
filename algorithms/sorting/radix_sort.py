words = ["test", "abc", "iip", "chinese", "france", "eason", "alan", "thimothy", "kfc", "python", "c", "programming"]
# words = ["test", "abc", "kfc", "c"]

max_letters = 11

def convert_to_numbers(words, max_letters):
    padding = ord('a')
    words_as_numbers = []

    for word in words:
        word_as_number = ""
        for letter in word:
            number = ord(letter) - padding
            word_as_number += str(number).zfill(2)

        n_letters = len(word)
        while n_letters < max_letters:
            word_as_number += "00"
            n_letters += 1

        words_as_numbers.append(word_as_number)

    return words_as_numbers

def convert_back(words, max_letters):
    padding = ord('a')
    converted_words = []

    for word in words:
        word_as_string = ""
        for block in range(2*max_letters):
            number = int(word[block:block+2])
            word_as_string += chr(padding + number)
            block += 2



def algorithm(converted_words, max_letters):
    for block_position in range(max_letters):
        counting_array = [0 for _ in range(26)]
        new_list = ["" for _ in range(len(converted_words))]

        for word in converted_words:
            i = 2 * max_letters - (block_position + 1) * 2
            j = i + 2
            last_block = word[i:j]
            last_block_number = int(last_block)
            counting_array[last_block_number] += 1

        for i in range(1, 26):
            counting_array[i] = counting_array[i] + counting_array[i-1]

        for word in reversed(converted_words):
            i = 2 * max_letters - (block_position + 1) * 2
            j = i + 2
            last_block = word[i:j]
            last_block_number = int(last_block)
            counting_array[last_block_number] -= 1
            new_list[counting_array[last_block_number]] = word

        converted_words = new_list

    return converted_words

converted_words = convert_to_numbers(words, max_letters)
sorted_words = algorithm(converted_words, max_letters)