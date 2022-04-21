import re
# print("""
# ** Welcome to Madlibs. If you don't know what that is, allow me to explain.                   **
# ** Madlibs is based on the idea of a user being prompted with a type of word                  **
# ** (Noun, Adjective, etc.) and based on the inputs will populate a fill in                    **
# ** the black document to make a story and because the user doesn't know the story beforehand, **
# ** the result is often humorous to read.                                                      **
# **                                                                                            **
# ** The way it will work here once fully fleshed out is it will prompt with a type of word     **
# ** on the command line and keep prompting until all the blanks have been filled.              **
# """)


def read_template(a):
    path = f"./{a}"
    with open(path) as file:
        contents = file.read() 
    print('file is closed?', file.closed)
    return contents

def parse_template(a):
    stripped_content = re.sub("{(.*?)}", '{}', a)
    content_parts = re.findall("{(.*?)}", a)
    unpack_tuple = (*content_parts,)
    new_tuple = (stripped_content, unpack_tuple)
    return new_tuple


def merge(a, b):
    story = a.format(*b)
    return story
