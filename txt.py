import os
class txt:
    def __init__(self, filesize, filename,generator,WORD_SEPARATOR):
        self.filesize = filesize
        self.filename = filename
        self.generator = generator
        self.word_separator = WORD_SEPARATOR

    def execute(self):
        for i in range(0,len(self.filename)):
            statinfo = 0
            file_size = int(self.filesize[i])
            file_name = self.filename[i]
            while statinfo < file_size:
                f = open(file_name,"a")
                temptxt = ""
                for i in range(0, 1000):
                    temptxt = temptxt + self.generator.generate(self.word_separator)
                f.write(temptxt + "/n")
                f.close()
                statinfo = os.stat(file_name).st_size
                print(statinfo)
                print(file_size)