import os #For Read Write Save
import speech_recognition as s #for Speech Recognition

class Model:
    #Initialize
    def __init__(self):
        self.key='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        self.offset=5

    #Encrytion of text
    def encrypt(self,plaintext):
        result=''
        for x in plaintext:
            try:
                i= (self.key.index(x)+self.offset)%62 #Total characters used
                result+=self.key[i]
            except ValueError:
                result+=x
            print(result)
        return  result

    #Decryption of cipher
    def decrypt(self,ciphertext):
        result=''
        for x in ciphertext:
            try:
                i=(self.key.index(x)-self.offset)%62
                result+=self.key[i]
            except ValueError:
                result+=x
        return result

    #Save File
    def save_file(self,msg,url):
        file=None
        result=None
        if type(url) is str:
            file=url
        else:
            file=url.name
        file_name,file_ext=os.path.split(file)
        print('url is:'+file)
        print(file_name)
        print(file_ext)
        print(file)
        if('.ntxt' in file_ext):
            result=self.encrypt(msg)
        else:
            result=msg
        with open(file,'w') as fl:
            fl.write(result)

    #Read From File
    def read_file(self,url):
        result=None
        file_name=os.path.basename(url)
        x,file_ext=os.path.splitext(url)
        if '.ntxt' in file_ext :
            fl=open(url,'r')
            result=self.decrypt(fl.read())
            fl.close()
        else:
            fl = open(url, 'r')
            result=fl.read()
            fl.close()

        return result,file_name

    #Save as Encrypted text
    def save_as(self,msg,url):
        file=None
        if type(url) is str:
            file=url
        else:
            file=url.name
        #print('url is:'+url)
        print('file is'+file)
        fl=open(file,'w')
        fl.write(self.encrypt(msg))
        fl.close()

    #Take input in voice format
    def takeQuery(self):
        print('in take query')
        sr=s.Recognizer()
        sr.pause_threshold=1
        with s.Microphone() as m:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='en-in')# hi-in for hindi
            print(query)
            return query




