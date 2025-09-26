from enum import Enum

class TipoCuenta(Enum):
    
    Ahorros = 1
    Corriente = 2

class CuentaBancaria:

    def __init__(self, NombresTitular: str, ApellidosTitular: str,NumeroCuenta: int, TipoCuenta: TipoCuenta):
    
        self.NombresTitular = NombresTitular
        self.ApellidosTitular = ApellidosTitular
        self.NumeroCuenta = NumeroCuenta
        self.TipoCuenta = TipoCuenta
        self.Saldo = 0.0

    def Imprimir(self):
        
        print("\nDatos de la cuenta:")
        print(f"Nombres del titular = {self.NombresTitular}")
        print(f"Apellidos del titular = {self.ApellidosTitular}")
        print(f"Número de cuenta = {self.NumeroCuenta}")
        print(f"Tipo de cuenta = {self.TipoCuenta.name}")
        print(f"Saldo = {self.Saldo}")

    def ConsultarSaldo(self):
        
        print(f"\nSaldo Acutal de la Cuenta: El saldo actual es de: ${self.Saldo}.")

    def Consignar(self, Valor: float):
       
        if Valor > 0:
            
            self.Saldo += Valor
            print(f"\nSe ha consignado ${Valor} en la cuenta."
                  f"El nuevo saldo en la cuenta es de ${self.Saldo}.")
            
            return True
        
        else:
            print("\nEl valor a consignar debe ser un valor mayor que cero.")
            
            return False

    def Retirar(self, Valor: float):
      
        if Valor > 0 and Valor <= self.Saldo:
            
            self.Saldo -= Valor
            print(f"\nSe ha retirado ${Valor} de la cuenta."
                  f"El saldo restante en la cuenta es de: ${self.Saldo}")
            
            return True
        
        else:
            print("\nEl valor a retirar debe ser menor o igual al saldo actual.")
            
            return False


class Ejercicio25:
    
    def main():
        
        Cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.Ahorros)
    
        Cuenta.Imprimir()
        
        print("\nPruebas: ")
        Cuenta.Consignar(200000)
        Cuenta.Consignar(300000)
        Cuenta.Retirar(400000)
        
        
if __name__ == "__main__":
    
    Ejercicio25.main()
    
    
