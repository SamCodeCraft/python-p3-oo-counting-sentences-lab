class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
            self.value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0
        
        # Split the string into sentences based on period, question mark, and exclamation mark
        sentences = [sentence.strip() for sentence in self.value.split('.') if sentence.strip()]
        sentences += [sentence.strip() for sentence in self.value.split('?') if sentence.strip()]
        sentences += [sentence.strip() for sentence in self.value.split('!') if sentence.strip()]
        return len(sentences)

string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())  
print(string.is_question())  
print(string.is_exclamation())  
print(string.count_sentences())  
