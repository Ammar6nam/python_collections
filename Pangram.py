def is_pangram (sentence):
    setAlphabet='abcdefghijklmnopqrstuvwxyz'
    psentence=sentence.lower()
    result=[]
    for x in setAlphabet:
        if x in psentence:
            result.append(True)
        else:
            result.append(False)
    if False in result:
        return False
    else:
        return True
sentence1=' Glib jocks quiz nymph to vex dwarf'
sentence2='Waltz, bad nymph, for quick jigs vex.'
sentence3= 'Sphinx of black quart, judge my vow.'
sentence4= 'How vexingly quick daft zebras jump!'
sentence5= 'The five boxing wizards jump quickly.'
sentence6= 'Jackdaws love my big sphinx of quartz.'
sentence7= 'Pack my box with five dozen liquor jugs.'
sentence8='abcdefghijklmnopqrstuvwxyz'
z1= is_pangram(sentence1)
z2= is_pangram(sentence2)
z3= is_pangram(sentence3)
z4= is_pangram(sentence4)
z5= is_pangram(sentence5)
z6= is_pangram(sentence6)
z7= is_pangram(sentence7)
z8=is_pangram(sentence8)
print(z1,z2,z3,z4,z5,z6,z7,z8,sep='\n')