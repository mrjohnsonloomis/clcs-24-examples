# core functionality: write/view notes, use file i/o, check to see if file exists
def add_note():
    with open('notes.txt', 'a') as file:
        new_note = input('Enter a note: ')
        file.write(new_note + '\n')

def view_notes():
    with open('notes.txt', 'r') as file:
        print(file.read())


add_note()
view_notes()
    
#read_lines() reads each lines as elements in list
#read_line() reads each line as a string (one at a time)
