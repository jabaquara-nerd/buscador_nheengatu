class Laptop:
    estado = "off"

    def ascender(self):
        self.estado = "ON"
        print(f"Laptop esta: {self.estado}")

    def desligar(self):
        self.estado = "OFF"
        print(f"Laptop esta: {self.estado}")

    def _explodir(self):
        print("BOOOM")

    def __repr__(self) -> str:
        return "Eh um laption"


class LaptopDell(Laptop):
    cor = "preto"
    marca = "Dell"

    def ascender(self):
        print("DELL esta ligad... tutruuru")


class LaptopLenovo(Laptop):
    marca = "Lenovo"


generico = Laptop()
print(generico)

# inspiron = LaptopDell()
# inspiron.ascender()

# carbonx = LaptopLenovo()
# carbonx.ascender()
# print(carbonx.estado)
# carbonx.desligar()
# print(carbonx.estado)
