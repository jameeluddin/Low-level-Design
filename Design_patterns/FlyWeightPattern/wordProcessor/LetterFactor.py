from Design_patterns.FlyWeightPattern.wordProcessor.DocumentCharacter import DocumentCharacter

char_cache = dict()

class LetterFactor:
    global char_cache


    def create_letter(self, char_value):
        print("aaa", char_cache)
        if char_cache.get(char_value):
            return char_cache.get(char_value)
        else:
            char_obj = DocumentCharacter(char_value, "Arial", 10)
            char_cache[char_value] = char_obj
            return char_obj
