class shankarSharma:
    wrap = "rumali roti"
    viggies = ["cabbage", "capsicum", "onion"]
    chiken_quality = "not bad"
    masala = ["x", 'y', 'z']

    def process (self):
        print("Finally chop grilled chicken with masala and veggies, wrapper")

    def get_masala (self):
        return self.masala

    def set_masala(self, new_masala):
        self.masala = new_masala   
        print(f" masala updated to: {self.masala}")


shankar = shankarSharma()
shankar.process()

print("Current masala:", shankar.get_masala()) 

shankar.set_masala(["a", "b", "c"])
print("Updated masala:", shankar.get_masala())