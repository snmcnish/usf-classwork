import numpy as np
import sys
import re

def load_glove(filename):

    word_to_vect_dict = {}

    readfile = open(filename, "r")

    for line in readfile:
        words = line.split()
        firstword = words[0]
        vector = np.array(map(float,words[1:]))
        word_to_vect_dict[firstword] = vector

    readfile.close()

    return word_to_vect_dict


def closest_words(gloves, word, n = 5):
    distances = []
    for key in gloves:
        dist = np.linalg.norm(gloves[word] - gloves[key])  # calculate distance between chosen word and all others
        distances.append((dist, key))  # gather distance and words in a list of tuple pairs

    distsort = sorted(distances)  # sort list of tuples by distance
    closest =  [i[1] for i in distsort[1:n + 1]]  # return word of the first n tuples
    return closest



def analogies(gloves, x, y, z, n = 5):
    xydist = np.subtract(gloves[x] , gloves[y])  # calculate distance between x and y
    distances = []
    for key in gloves:
        if z != key:
            zdist = np.subtract(gloves[z] , gloves[key])  # calculate distance between z and all others

            xyzdist = np.linalg.norm(np.subtract(zdist , xydist))  # calculate distance between x-y distance and z to all others words distances

        distances.append((xyzdist, key))

    distsort = sorted(distances)  # sort list of tuples by distance
    closest = [i[1] for i in distsort[0: n ]]  # return word of the first n tuples

    return closest

if __name__ == '__main__':
    glove_filename = sys.argv[1]
    gloves = load_glove(glove_filename)

    print("Enter a word or 'x:y as z:'")
    cmd = raw_input("> ")
    while cmd != None:
        match = re.search(r'(\w+):(\w+) as (\w+):', cmd)
        if match is not None and len(match.groups()) == 3:
            x = match.group(1).lower()
            y = match.group(2).lower()
            z = match.group(3).lower()
            words = analogies(gloves, x, y, z)
            print "%s is to %s as %s is to {%s}" % (x, y, z, ' '.join(words))
        elif re.match(r'\w+', cmd) is not None:
            words = closest_words(gloves, cmd)
            print "%s is similar to {%s}" % (cmd, ' '.join(words))
        else:
            print("Enter a word or 'x:y as z:'")
        cmd = raw_input("> ")