def boyer_horspool(wildcard, pattern, string):
    pattern_length = len(pattern)
    string_length = len(string)
    table = {}

    #checking for empty strings
    if pattern_length*string_length == 0:
        print("empty string or pattern")
        return

    #pre-processing
    for i in range(0,pattern_length - 1):
        table[pattern[i]] = pattern_length - i -1

    k = pattern_length - 1
    position = 0
    occurrence = 0

    #searching
    while (position + k  < string_length):
        if(string[position + k] == pattern[k] or pattern[k] == wildcard):
            k = k-1
        else:
            #shifting
            if (wildcard in table):
                wildcard_position = table[wildcard]
                if (string[position + pattern_length - 1] in table):
                    letter_position = table[string[position + pattern_length - 1]]
                    if(wildcard_position < letter_position): #shift the shortest distance possible
                        position = position + wildcard_position
                    else:
                        position = position + letter_position
                else:
                    position = position + wildcard_position
            else:
                if (string[position + pattern_length - 1] in table):
                    letter_position = table[string[position + pattern_length - 1]]
                    position = position + letter_position
                else:
                    position = position + pattern_length
            k = pattern_length -1
        if(k<0):
            print("pattern exists @ " + str(position))
            occurrence = occurrence +1
            k = pattern_length - 1
            position = position +1
    if occurrence == 0:
        print("No match.")
    else:
        print("No of occurrences:"+ str(occurrence))