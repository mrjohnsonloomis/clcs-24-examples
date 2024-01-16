def every_other(text):
    new_text = ''
    for i in range(0, len(text), 2):
        new_text += text[i]
    return new_text

print(every_other('cattywampus'))