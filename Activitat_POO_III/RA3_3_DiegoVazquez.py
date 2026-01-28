"""
Autor: Diego Vazquez Perez
Data: 28-01-2026
Descripció: Exercici 3. Refactorització de CarretCompra per utilitzar el patró Estratègia (Strategy Pattern) per als descomptes, eliminant la lògica hardcoded.
"""

# ==========================================
# CODI ORIGINAL (Lògica Hardcoded)
# ==========================================
"""
class CarretCompra:
    def __init__(self, total):
        self.total = total

    def calcular_total_amb_descompte(self):
        descompte = self.total * 0.20 # 20% fix
        return self.total - descompte
"""

# ==========================================
# CODI REFACTORITZAT (Strategy Pattern)
# ==========================================

class Descompte20:
    def aplicar(self, total):
        return total * 0.20

class SenseDescompte:
    def aplicar(self, total):
        return 0

class DescompteFix10Euros:
    def aplicar(self, total):
        return 10 if total >= 10 else total

class CarretCompra:
    def __init__(self, total, estrategia_descompte):
        self.total = total
        # Injecció de l'estratègia de descompte
        self.estrategia_descompte = estrategia_descompte

    def calcular_total_amb_descompte(self):
        # Delegació del càlcul del descompte a l'estratègia
        descompte = self.estrategia_descompte.aplicar(self.total)
        return self.total - descompte

if __name__ == "__main__":
    total_compra = 100

    print("--- Test amb Descompte20 ---")
    estrategia_20 = Descompte20()
    carret1 = CarretCompra(total_compra, estrategia_20)
    print(f"Total original: {total_compra}, Total amb descompte: {carret1.calcular_total_amb_descompte()}")

    print("\n--- Test amb SenseDescompte ---")
    estrategia_sense = SenseDescompte()
    carret2 = CarretCompra(total_compra, estrategia_sense)
    print(f"Total original: {total_compra}, Total amb descompte: {carret2.calcular_total_amb_descompte()}")

    print("\n--- Test amb DescompteFix10Euros ---")
    estrategia_fix = DescompteFix10Euros()
    carret3 = CarretCompra(total_compra, estrategia_fix)
    print(f"Total original: {total_compra}, Total amb descompte: {carret3.calcular_total_amb_descompte()}")
