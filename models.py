from string import ascii_letters ,ascii_lowercase, ascii_uppercase, punctuation
class PasswordChecker:
    def __init__(self, username, password, birthday):
        self.username = username
        self.password = password
        self.birthday = birthday
        self.score = 0

    
    def length_of_letters(self):
        '''This function gets the length of the password and 
        returns a score if it is greater than 8.'''
        if len(self.password) >= 8:
            self.score += 1

        
    def contain_letter_english(self):
        ''''''
        for char in self.password:
            if char in ascii_letters:
                self.score += 1


    def contains_special_characters(self):
        for char in self.password:
            if char in punctuation:
                self.score += 1


    def contains_uppercase_letter(self):
        for char in self.password:
            if char in ascii_uppercase:
                self.score += 1


    def has_username(self):
        if self.username not in self.password:
            self.score += 1
    

    def has_swapcase_usernaem(self):
        if self.username.swapcase not in self.password:
            self.score += 1
        
    
    def replace_with_special_char(self):
        ...
    
