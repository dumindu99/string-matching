import algorithm
import os

print("--- Data Structures & Algorithms III ---")
print("String Matching Assignment")
print("Index: 19000197")
print()

stop = False
while (not stop):
    print("######## MENU ##########")
    print("Select the action:")
    print("1)Give inputs manually")
    print("2)Load tests")
    print("3)Exit")
    txt = input("input(1/2/3)>")
    print("##########################")
    if(txt == "3"):
        stop = True
    elif (txt == "1"):
        wildcard = input("Enter the wildcard:")
        pattern = input("Enter the pattern:")
        search_text = input("Enter the text:")
        print("######## RESULT ##########")
        algorithm.boyer_horspool(wildcard, pattern, search_text)
        print("##########################")
    else:
        print("######## TESTS ##########")
        entries = os.scandir('tests/')
        i = 1
        for file in entries:
            print(str(i)+ ") "+ file.name + "-----------------")
            test_file = open('tests/'+file.name, 'r')
            print("Wildcard: "+test_file.readline().rstrip('\n')+ " Pattern: "+ test_file.readline().rstrip('\n'))
            print("Text: "+ test_file.readline().rstrip('\n'))
            test_file.close()
            i = i+1

        print("##########################")
        number = input("Select the test file (enter the file number):")
        entries = list(os.scandir('tests/'))
        selected_file = open("tests/" + entries[int(number) - 1].name, 'r')
        wildcard = selected_file.readline().rstrip('\n')
        pattern = selected_file.readline().rstrip('\n')
        search_text = selected_file.readline().rstrip('\n')
        print("######## RESULT ##########")
        algorithm.boyer_horspool(wildcard,pattern,search_text)
        print("##########################")