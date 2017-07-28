def mutate_string(string, position, character):
    string = list(string)
    string[position]=character
    return ''.join(string)

print mutate_string('abracadabra',5,'k')