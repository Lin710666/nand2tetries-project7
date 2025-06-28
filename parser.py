#CLASS
class Parser:
    def __init__(self,file):
        self.file = file
        self.lines = []
        self.commands = []
       


    def get_commands(self):
        file = open(self.file, 'r')
        self.lines = file.readlines()
        file.close()
         

    def rm_comments(self):
        for i in range(len(self.lines)):
            self.lines[i] =    self.lines[i].split('//')[0]          


    def rm_new_line(self):
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i].split('\n')[0]

    def rm_blank_line(self):
        for line in self.lines:
            if line != "":
                self.commands.append(line)

    def get_code(self):
        self.get_commands()
        self.rm_comments()
        self.rm_new_line()
        self.rm_blank_line()
        return self.commands


           
        


            



        
