class Codex:
    def __init__(self, text, step):
        self.text = text
        self.step = step

    def encrypt_method(self):
        encrypted_str = ""
        for char in self.text:
            if not char.isalpha():
                encrypted_str += chr(((ord(char) + self.step - 32) % 15) + 32)
            elif char.isupper():
                encrypted_str += chr(((ord(char) + self.step - 65) % 26) + 65)
            else:
                encrypted_str += chr(((ord(char) + self.step - 97) % 26) + 97)
        return encrypted_str

    def decrypt_method(self):
        decrypted_str = ""
        for char in self.encrypt_method():
            if not char.isalpha():
                decrypted_str += chr(((ord(char) - self.step - 32) % 15) + 32)
            elif char.isupper():
                decrypted_str += chr(((ord(char) - self.step - 65) % 26) + 65)
            else:
                decrypted_str += chr(((ord(char) - self.step - 97) % 26) + 97)
        return decrypted_str

    
text1 = Codex("Star Trek: The Next Generation!", 2)
print(text1.encrypt_method(), "=", text1.decrypt_method())

