'''
Creates a function that takes text and outputs a dictionary of currencies
to their (or their curr_dic variants') frequency in the text.
'''
from curr_dic import curr_lis

# Construct a dictionary of currency combinations ('USDMXN')
combo_lis = []
for c1 in curr_lis:
    for c2 in [curr for curr in curr_lis if curr!=c1]:
        combo_lis.append((c1+c2))

def curr_occur(text):
    '''
    Returns a dictionary of {CURR: num},
    where num is the count of occurences of curr in the text
    '''
    out_dic = {c:0 for c in curr_lis}
    for curr in curr_lis:
        out_dic[curr] += text.count(' '+curr+' ')

    for combo in combo_lis:
        if combo in text:
            out_dic[combo[:3]] += text.count(combo)
            out_dic[combo[3:6]] += text.count(combo)

    return out_dic


if __name__ == '__main__':
    curr_occur()
