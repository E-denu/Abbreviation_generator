from Denu_Preprocessing import comp_word_separation
from Denu_Preprocessing import eject_puncs
from Denu_Preprocessing import smallscore_SelectOnewordname
from Denu_Preprocessing import  smallscore_ManywordName

def Abbreviation(name_txt):

    '''The main function that will be used to generate the abbreviations. It takes a text file as 
    an input and returns the lowest valid score abbreviation for each name in the text file.
    Below is the implementation using the imported functions that gradually works to achieve the set goals'''

    hyphens = ["-", "_"]
    #First cleaning the and separating all compound words
    cleaned_names = eject_puncs(name_txt)
    letters = []
    abbr = []
    # Splitting compound names and selecting least scores
    for word in cleaned_names:
        str_ = ''
        if any(x in word for x in hyphens):
            sep = comp_word_separation(comp_name=word)
            letters.append(sep)
            if len(sep) > 2:
                str_ += sep[0][0] + sep[1][0] + sep[2][0]
                abbr.append(word)
                abbr.append(str_)
            elif len(sep) == 2:
                str_ += sep[0][0] + sep[1][0] + sep[1][1]
                abbr.append(word)
                abbr.append(str_)
        else:
            each = word.split() 
            if len(each) > 2: 
                str_ += each[0][0] + each[1][0] + each[2][0]
                abbr.append(word)
                abbr.append(str_)
            elif len(each) == 2:
                last_num = lambda y: each[1][-1] if (each[1][-1]!='E') else smallscore_ManywordName(each[-1])
                str_ += each[0][0] + each[1][0] + last_num(each)
                abbr.append(word)
                abbr.append(str_)
            #selecting least scores for one word names
            elif len(each) == 1:
                chars = each[0]
                str_ += each[0][0] + smallscore_SelectOnewordname(chars)
                abbr.append(word)
                abbr.append(str_)
    print(abbr)

    #Specifying an output file name starting with my surname
    file_name = name_txt.split('.')[0]
    myname = 'Denu'
    output_filename = "{}_{}_abbrevs.txt".format(myname.lower(),file_name.lower())  #(f'{myname.lower()}_{file_name.lower()}_abbrevs.txt')
    
    #Writing final results to the output file
    with open(output_filename, 'w') as final_file:
        final_file.write('\n'.join(abbr)) 

#running the function if it is in the main scope
if __name__ == '__main__':
    file_name = input('Enter file name: ')
    Abbreviation(name_txt=file_name)