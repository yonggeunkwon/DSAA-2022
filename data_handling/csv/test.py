def what(sentence):
    return sentence.replace(" ", "").replace("\n", "").replace("\t", "")

print(what("Hello, This is \n CS50. "))