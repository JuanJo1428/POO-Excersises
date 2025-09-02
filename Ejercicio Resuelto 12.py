# Ejercicio Número 12

class SR:
    
    @staticmethod
    def CalcularBruto(HorasTrabajadas, ValorHora):
        SalarioB = HorasTrabajadas * ValorHora
        return SalarioB
    
    @staticmethod
    def CalcularPorcentajeR(Retencion):
        PorcentajeRetencion = Retencion / 100
        return PorcentajeRetencion
    
    @staticmethod
    def CalcularValorRetencion(SalarioBruto, PorcentajeRetencion):
        Retencion = SalarioBruto * PorcentajeRetencion
        return Retencion
    
    @staticmethod
    def CalcularNeto(SalarioBruto, Retencion):
        SalarioN = SalarioBruto - Retencion
        return SalarioN
    
class Ejericio_12:
    
    def ValorSalarioBN():
        
        HorasTrabajadas = float(input("Ingresa el número de horas trabajadas: "))
        ValorHora = float(input("Ingrese el valor por hora: "))
        Retencion = float(input("Ingrese el valor de la retencion en la fuente: "))

        SalarioBruto = SR.CalcularBruto(HorasTrabajadas, ValorHora)
        PorcentajeRetencion = SR.CalcularPorcentajeR(Retencion)
        ValorRetencion = SR.CalcularValorRetencion(SalarioBruto, PorcentajeRetencion)
        SalarioNeto = SR.CalcularNeto(SalarioBruto, ValorRetencion)

        print(f"El Salario Bruto del trabajador es de ${SalarioBruto}.")
        print(f"Pero  al tener una Retención en la fuente de ${ValorRetencion}, en realidad su Salario Neto es de ${SalarioNeto}.")
        

Ejericio_12.ValorSalarioBN()

