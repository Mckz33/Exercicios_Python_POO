class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        self.canal = canal
    def getVolume(self):
        return self.volume
    def aumentarVolume(self, volume):
        self.volume += volume
    def diminuirVolume(self, volume):
        self.volume -= volume