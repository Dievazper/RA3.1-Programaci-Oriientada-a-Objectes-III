"""
Autor: Diego Vazquez Perez
Data: 28-01-2026
Descripció: Exercici 1. Refactorització de la classe Factura per eliminar l'acoplament fort amb ImpressoraPDF mitjançant injecció de dependències.
"""

# ==========================================
# CODI ORIGINAL (Alt Acoplament)
# ==========================================
"""
class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class Factura:
    def __init__(self, client, import_total):
        self.client = client
        self.import_total = import_total
        self.impressora = ImpressoraPDF() # Acoplament directe

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)
"""

# ==========================================
# CODI REFACTORITZAT (Baix Acoplament)
# ==========================================

# Interfície implícita (Duck Typing) per a Impressora
class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class ImpressoraText:
    """Una altra implementació d'impressora per demostrar flexibilitat."""
    def imprimir(self, contingut):
        print(f"Imprimint TEXT: {contingut}")

class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        # Injecció de dependència: la impressora arriba des de fora
        self.impressora = impressora

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        # Delegació de responsabilitat
        self.impressora.imprimir(contingut)

if __name__ == "__main__":
    print("--- Test amb ImpressoraPDF ---")
    impressora_pdf = ImpressoraPDF()
    factura1 = Factura("Client A", 100, impressora_pdf)
    factura1.imprimir_factura()

    print("\n--- Test amb ImpressoraText (canvi d'implementació sense tocar Factura) ---")
    impressora_text = ImpressoraText()
    factura2 = Factura("Client B", 200, impressora_text)
    factura2.imprimir_factura()
