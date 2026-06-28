from string import ascii_letters ,ascii_lowercase, ascii_uppercase, punctuation
class PasswordChecker:
    def __init__(self, username:str, password:str, birthday:str="None"):
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
        flag = False
        for char in self.password:
            if char in ascii_letters:
                flag = True
        if flag:
            self.score += 1


    def contains_special_characters(self):
        flag = False
        for char in self.password:
            if char in punctuation:
                flag = True
        
        if flag:
            self.score += 1


    def contains_uppercase_letter(self):
        flag = False
        for char in self.password:
            if char in ascii_uppercase:
                flag = True
        
        if flag:
            self.score += 1

    def has_username(self):
        if self.username not in self.password:
            self.score += 1
    

    def has_swapcase_username(self):
        if self.username.swapcase() not in self.password:
            self.score += 1
        
    
    def replace_with_special_char(self):
        special_character = {
            "@" : "a",
            "!" : "i",
            "0" : "o",
            "$" : "s"
        }

        username_ = self.username.lower()
        password_ = self.password.lower()


        for special_char , char in special_character.items():
            username_ = username_.replace(special_char, char)
        
        for special_char, char in special_character.items():
            password_ = password_.replace(special_char, char)
        
        if username_ in password_:
            return None
        else:
            self.score += 1


    def password_similar_common_passwords(self):
        common_password = "123456", "12345678", "12345", "111111", "123456789", "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd"

        if self.password not in common_password:
            self.score += 1