'''In the check_questionMark function, the for loop iterates through the list given as a parameter.
 If one of the words contains a question mark, the if loop prints that word followed by a message
 The checkCommonChar function identifies common characters in the list parameter using by loops to
 iterate through the list and adding them to a set. It counts the number of times
 common characters appear by appending them to the freq_listing set and
 printing the elements'''

list01 = ['farshad', 'ghassemi?d', 'madam', '?radar?', 'duration', 'con?tained']


def check_questionMark(word_list):
    print("Question marks check:")
    for word in word_list:
        if '?' in word:
            print(word, "contains a question mark")

def checkCommonChar(word_list):
    common  =set()
    print("Common character check:")
    for word in word_list:
        if not common:
            [common.add(ch) for ch in word]
        else:
            common = set(list(word)).intersection(common)
    
    freq_listing = {}
    for word in word_list:
        for ch in list(common):
            if ch in word:
                ch_count = word.count(ch)
                fmt_str = f"{word} contains {ch_count} {ch}"
                if ch in freq_listing:
                    freq_listing[ch].append(fmt_str)
                else:
                    freq_listing[ch] = [fmt_str]
    
    for k, v in freq_listing.items():
        print(f"Character {k} appears in all items")
        for fmt in v:
            print(fmt)


def main():
    check_questionMark(list01)
    print("\n\n")
    checkCommonChar(list01)

main()

