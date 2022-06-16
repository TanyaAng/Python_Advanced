def concatenate (*args, **kwargs):
    text=''
    for word in args:
        text+=word
    for key,value in kwargs.items():
        if key in text:
            text=text.replace(key,value)
    return text

# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))