def main():
    print("Welcome to Text Manipulation Program!", "Press 1 to add data", "Press 2 to display data", "Press 3 to count the number of vowels, words, consonants & digits", "Press 4 to search for a word", "Press 5 to display the size and the number of lines", sep="\n")


def addData(filename):
    text = input("Enter the text below:\n")
    open(filename, "w").write(text)
    open(filename, "w").close()

def displayData(filename):
    print(open(filename, "r").read())

def counter(filename):
    vow, cons, word, num = 0, 0, 0, 0
    for i in (open(filename, "r").read().split()):
        word+=1
        for j in i:
            if(j.lower() in "aeiou"):
                vow+=1
            elif(j.lower() not in "aeiou" and j.isalnum()):
                cons+=1
            elif(j.isnumeric):
                num+=1
    print("Vowels:", vow, "\nConsonants:", cons, "\nWords", word, "\nNumbers:", num)

def wordSearch(filename):
    search = input("Enter a word to search:\n")
    flag = 0
    for i in (open(filename, "r").read().split()):
        if i==search:
            flag = 1
    if(flag==1):
        print("Got it!")
    else:
        print("Not Found")

def sizeNumber(filename):
    line_count = 0
    with open(filename, "r") as file:
        for line in file:
            line_count+=1
