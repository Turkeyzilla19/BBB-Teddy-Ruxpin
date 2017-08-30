class talk:
    def __init__(self,func):
        words = raw_input("what words do you want? ")

        self.talkFunc = func        
        def speak():
            self.talkFunc( words )
