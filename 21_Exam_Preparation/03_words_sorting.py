def words_sorting(*args):
    words_dictionary={}
    for word in args:
        if word not in words_dictionary:
            words_dictionary[word]=0
        ascii_result=0
        for ch in word:
            ascii_result+=ord(ch)
        words_dictionary[word]+=ascii_result
    result=''
    if sum(words_dictionary.values())%2==0:
        for key,value in sorted(words_dictionary.items(), key=lambda kvp: (kvp[0])):
            result+=f'{key} - {value}\n'
    else:
        for key,value in sorted(words_dictionary.items(), key=lambda kvp: (-kvp[1])):
            result+=f'{key} - {value}\n'
    return result


