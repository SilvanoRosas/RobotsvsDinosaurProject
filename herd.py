from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    def create_herd(self):
        dino1 = Dinosaur("Stegosaurus", 8)
        dino2 = Dinosaur("Raptor", 15)
        dino3 = Dinosaur("T-Rex", 50)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)