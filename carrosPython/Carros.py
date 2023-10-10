class Carro:
    def __init__(self):
        self.motor_ligado = False
        self.esta_andando = False

    def ligar_motor(self):
        if not self.motor_ligado:
            self.motor_ligado = True
            print("Motor ligado.")
        else:
            print("O motor já está ligado.")

    def desligar_motor(self):
        if self.motor_ligado:
            if not self.esta_andando:
                self.motor_ligado = False
                print("Motor desligado.")
            else:
                print(
                    "Não é possível desligar o motor enquanto o carro está em movimento. Pare o carro primeiro.")
        else:
            print("O motor já está desligado.")

    def andar(self):
        if self.motor_ligado and not self.esta_andando:
            self.esta_andando = True
            print("O carro está em movimento.")
        elif not self.motor_ligado:
            print("O motor está desligado. Ligue o motor primeiro.")
        else:
            print("O carro já está em movimento.")

    def parar(self):
        if self.esta_andando:
            self.esta_andando = False
            print("O carro parou.")
        else:
            print("O carro já está parado.")


if __name__ == '__main__':
    carro = Carro()
    carro.ligar_motor()
    carro.andar()
    carro.parar()
    carro.desligar_motor()
