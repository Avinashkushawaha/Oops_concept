from abc import ABC, abstractmethod

class playable(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(playable):
    def play(self):
        print("playing the quiter")    

class Piano(playable):
    def play(self):
        print("playing the piano")

guitar = Guitar()                
piano = Piano()

guitar.play()
piano.play
