"""
--- Day 2: Inventory Management System Part 2---

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. 
For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). 
However, the IDs fghij and fguij differ by exactly one character, the third (h and u). 
Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by 
removing the differing character from either ID, producing fgij.)
"""

def parse_input(dtype=str):

    return [dtype(line.rstrip('\n')) for line in open('input.txt')]

data = parse_input()

def main():

    data_sep_list = []
    for datum in data:
        str_list = []
        for k in range(26):
            str_list.append(datum[k])
        data_sep_list.append(str_list)

    done = False
    for k in range(len(data_sep_list)):
        if not done:
            count = 0
            for j in range(len(data_sep_list)):
                list_common = []
                for a, b in zip(data_sep_list[k], data_sep_list[j]):
                    if a == b:
                        list_common.append(a)     
                if len(data_sep_list[k]) - len(list_common) == 1:
                    print "we have a match"
                    done = True
                    print '.'.join(data_sep_list[k]) 
                    print '.'.join(data_sep_list[j])
                    print '.'.join(list_common)
                    break


if __name__ == '__main__':

    main()

        


   

