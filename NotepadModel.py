import os
import speech_recognition as s


class Model:
    def __init__(self):
        self.key = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.offset = 5

    def encrypt(self, plaintext):
        result = ''
        for ch in plaintext:
            try:
                i = (self.key.index(ch) + self.offset) % 62  # 62
                result += self.key[i]
            except ValueError:
                result += ch

        return result

    def decrypt(self, cyphertext):
        result = ''
        for ch in cyphertext:
            try:
                i = (self.key.index(ch) - self.offset) % 62  # (self.key.length())
                result += self.key[i]
            except ValueError:
                result += ch

        return result

    def save_file(self, msg, url):  # splittext
        if type(url) is not str:
            file = url.hostname
        else:
            file = url

        filename, file_extension = os.path.splitext(file)
        if file_extension in '.ntxt':
            content = msg
            encrypted = self.encrypt(content)
            with open(file, 'w') as fw:
                fw.write(encrypted)
        else:
            content = msg
            with open(file, 'w')as fw:
                fw.write(content)

        # if file_extension in '.ntxt':
        # msg=self.encrypt(msg)
        # with open(file,'w')as fw:
        # fw.write(msg

    def save_as(self, msg, url):
        if type(url) is not str:
            file = url.name
        else:
            file = url
        msg = self.encrypt(msg)
        with open(file, 'w')as fw:
            fw.write(msg)

    def read_file(self, url):
        base = os.path.basename(url.name)
        filename, file_extension = os.path.splitext(base)
        if file_extension in '.ntxt':
            fi = open(url.name, "r")
            msg1 = fi.read()
            decrypted = self.decrypt(msg1)
            fi.close()
            return decrypted, base
        else:
            fi = open(url.name, "r")
            msg1 = fi.read()
            fi.close()
            return msg1, base

    def takeQuery(self):
     pass
#needs improvement

# To check scrollbar or any method is being called or not
# Two CLasses Scrollbar and text,,,,make  your classes and override methods and give your functonality ,this way
# You can check whether it is called or not via coding
