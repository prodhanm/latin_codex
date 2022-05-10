class Codex:
    def __init__(self, text, step):
        self.text = text
        self.step = step

    def encrypt_method(self):
        encrypted_str = ""
        for char in self.text:
            if not char.isalpha():
                encrypted_str += char
            elif char.isupper():
                encrypted_str += chr(((ord(char) + self.step - 65) % 26) + 65)
            else:
                encrypted_str += chr(((ord(char) + self.step - 97) % 26) + 97)
        return encrypted_str
text1 = Codex("Trustn01!", 2)
print(text1.encrypt_method())

