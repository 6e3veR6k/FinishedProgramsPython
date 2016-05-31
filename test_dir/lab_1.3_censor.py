def censor(text_line, word):

    text_to_list = text_line.split(" ")  # create a list with words

    word_to_asterisks = "*"*len(word)

    for i in text_to_list:
        if word in text_to_list:

            removeble_word = text_to_list.index(word)

            text_to_list.remove(word)

            text_to_list.insert(removeble_word, word_to_asterisks)




    return " ".join(text_to_list)










censor("this hack is wack hack", "hack")