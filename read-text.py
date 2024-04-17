# Program reads the content of a text file

def read_text(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

file_name = 'text.txt'
content = read_text(file_name)
print(content)