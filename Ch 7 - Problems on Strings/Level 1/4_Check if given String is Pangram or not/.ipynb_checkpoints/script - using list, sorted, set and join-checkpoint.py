test_pangram_positive = [
    "The quick brown fox jumps over the lazy dog.",
    "Waltz, bad nymph, for quick jigs vex.",
    "Glib jocks quiz nymph to vex dwarf.",
    "Sphinx of black quartz, judge my vow.",
    "How quickly daft jumping zebras vex!",
    "The five boxing wizards jump quickly.",
    "Jackdaws love my big sphinx of quartz.",
    "Pack my box with five dozen liquor jugs."
]

test_pangram_negative = [
    "My name is Ashish.",
    "I love programming.",
    "Am from Delhi and brown fox jumps over the dog."
]


def check_pangram(in_str):
    in_str = in_str.lower()
    in_str = [x for x in in_str if x.isalpha()]
    in_str = sorted(in_str)
    in_str = set(in_str)

    ret_val = False
    if(len(in_str) == 26):
        ret_val = True
    
    return ret_val 


for i in test_pangram_positive:
    print(check_pangram(i))

for i in test_pangram_negative:
    print(check_pangram(i))
