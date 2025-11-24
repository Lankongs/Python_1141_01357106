import re
import myFunctions

def main():
    file = open("input.txt","r+",encoding="utf-8")
    content = file.read() 
    words = re.findall(r'\b[a-zA-Z]+\b', content)
    file.close()

    mostwords = {}
    mostletter = {}
    for word in words:
        myFunctions.analyze(word, mostwords, mostletter)
    
    sorted_words, sorted_letter = myFunctions.sortAnswer(mostwords, mostletter)
    myFunctions.printAnswer(sorted_words, sorted_letter)
    

if __name__ == "__main__":
    main()
