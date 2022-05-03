# Given a sentence - "Benedict Cumberbatch cannot say the word penguin correctly."
# Once a letter has occurred in the sentence, replace all of its following occurrences with '_', then return the sentence
# bonus challenge: count uppercase and lowercase letters as the same

sentence = "Benedict Cumberbatch cannot say the word penguin correctly."
def whiteboard(sen):
    seen_ls=[]
    for i in sen:
        if i.lower() not in str(seen_ls).lower():
            seen_ls.append(i)
        else:
            seen_ls.append('_')
    return ("").join(seen_ls)
print(whiteboard(sentence))
