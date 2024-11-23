class ShankarSharma:
    masala = ["x", "y", "z"]

    @property 
    def masala(self):
        print("Cannot access the private number")

    @masala.setter
    def masala(self, new_masala):
        print("Cannot modify the private number")


plate1 = ShankarSharma()
plate1.masala
plate1.masala = ["a", "b", "c"]       
