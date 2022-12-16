
def eject_puncs(myfile):
    
    '''All punctuations on the names must be removed, hence the following are dictionaries of 
    punctuations and letters with their scores, as well as characters used to create compound names
    indicated as hyphens. These will be used in the functions below during processing'''
    
    common_punctuation = {"'":"","*":"","+":"","^":"","!":"","%":"","’":"","`":"","&":""}
    '''The eject_puncs function is used to remove all possible punctuations from the names'''
    
    with open(myfile, 'r') as opened_file:
        content = opened_file.read().split('\n') 
    removed_puncts = []
    '''This loops through wach word to remove any punctuations specified in the
    common_punctuation dictionary'''
    # Looping through each word and removing non-letter characters defined in the dictionary
    for name in content:
        removing_puncs = name.translate(str.maketrans(common_punctuation)).upper()
        removed_puncts.append(removing_puncs)
    removed_puncts
    return removed_puncts


def comp_word_separation(comp_name):
    '''The comp_word_separation function will split all compound words based on separators in hyphens'''
    hyphens = ["-", "_"]
    separated = []
    if len(comp_name.split()) > 1:
        '''This loops through the names and separate them based on space'''
        for words in comp_name.split():
            for hyphen in hyphens:
                '''This checks whether there is a character in hyphen present in the names
                if so, that name is splitted by that character'''
                if hyphen in words:
                    splitted=words.split(hyphen)
                    separated  += splitted
                else:
                    pass
        '''Finally, all names that are not compound names are then added to then separated list'''
        separated.append(words)
    elif len(comp_name.split()) == 1:
        for words in comp_name.split():
            for hyphen in hyphens:
                if hyphen in words:
                    splitted=words.split(hyphen)
            separated+=splitted
    return separated


letter_score = {
'A':25, 'B':8, 'C':8, 'D': 9, 'E':35, 'F':7, 'G':9, 'H':7, 'I':25, 'J':3,
'K':6, 'L':15, 'M':8, 'N':15, 'O':20, 'P':8, 'Q':1, 'R':15, 'S':15, 'T':15, 
'U':20, 'V':7, 'W':7, 'X':3, 'Y':7, 'Z':1}

def smallscore_SelectOnewordname(str_name):

    '''The smallscore_SelectOnewordname function is used to select the least valid score abbreviations
    from one word names'''
    splitted = [*str_name]
    abb_dict = {}
    for key,value in letter_score.items():
        if key in splitted:
            abb_dict[key] = value
            
    list_keys = list(abb_dict.keys())
    list_values = list(abb_dict.values())
    numbers = []
    for key in splitted[1:]:
        numbers.append(abb_dict[key])
    numbers.sort()

    first_char = numbers[0]
    second_char = numbers[1]
    first_value = list_values.index(first_char)
    second_value = list_values.index(second_char)
    combined_char = list_keys[first_value] + list_keys[second_value]
    
    arr = []
    splitted2 = [*str_name]
    splitted3 = [*combined_char]
    arr.append(splitted2.index(splitted3[0]))
    arr.append(splitted2.index(splitted3[1]))
    arr.sort()
    return splitted2[arr[0]]+splitted2[arr[1]]

def smallscore_ManywordName(str_name1):
    '''The smallscore_ManyWordsName function is used to select small abbreviations with
    the least scores in names that contain more than one word'''
    splitted = [*str_name1]
    abb_dict = {}
    for key,value in letter_score.items():
        if key in splitted:
            abb_dict[key] = value
            
    list_keys = list(abb_dict.keys())
    list_values = list(abb_dict.values())
    numbers = []
    for key in splitted[1:]:
        numbers.append(abb_dict[key])
    numbers.sort()

    first_char = numbers[0]
    first_value = list_values.index(first_char)
    comb_char = list_keys[first_value]
    return comb_char

