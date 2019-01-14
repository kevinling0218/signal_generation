from curr_dic import curr_dic, curr_lis
import re
def curr_replacer(text):
    '''
    Using the curr_dic form curr_dic, replaces phrases in text with their currencies.
    '''
    text = ' '+text+' '
    # Create a list of phrases in curr_dic in descending order, so we replace larger substrings first
    phrase_list = list(curr_dic.keys())
    phrase_list.sort(key = lambda phrase: 1/len(phrase))

    for phrase in phrase_list:
        text = text.replace(phrase, ' '+curr_dic[phrase]+' ')


    return text

if __name__ == '__main__':
    curr_replacer()
