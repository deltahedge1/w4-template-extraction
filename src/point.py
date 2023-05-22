import re

class Point:
    def __init__(self, x0, y0, x1, y1, label):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.label = label
    
    @property
    def cleaned_value(self, value):
        # Escape special characters in the sentence for regex matching
        sentence_regex = re.escape(self.label)
        
        # Create the regex pattern to match the sentence
        pattern = r"(?s)\b{}\b.*?(?=\b|$)".format(sentence_regex)
        
        # Remove the sentence from the text
        result = re.sub(pattern, "", self.value)
        
        return result

    @property
    def coordinates(self):
        return (self.x0, self.y0, self.x1, self.y1)