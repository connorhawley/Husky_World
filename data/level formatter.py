import os

def format_level():
    
    print("Example path format: C:/Users/Connor/Desktop/level.txt")
    print("Make sure the text in the file only what is contained inside the [] brackets.")
    textpath = input("Input level text file path: ")
    every = int(input("Enter level width: "))
    file = open(textpath, "r")
    string = file.read()
    string = string.replace(", ", "")
    string = string.replace("0", " ")
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    desktop = desktop + "/formattedlevel.txt"
    formattedlevel = open(desktop, 'w')
    newstring = '",\n"'.join(string[i:i+every] for i in range(0, len(string), every))
    newstring = '["' + newstring + '",]'
    
    formattedlevel.write(newstring)
    file.close()
    formattedlevel.close()
    print("Level formatted. Output to Desktop/formattedlevel.txt")
