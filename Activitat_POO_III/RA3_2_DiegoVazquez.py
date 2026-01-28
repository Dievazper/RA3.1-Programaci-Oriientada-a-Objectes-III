"""
Autor: Diego Vazquez Perez
Data: 28-01-2026
Descripció: Exercici 2. Refactorització de la classe Comanda perquè el Notificador sigui injectat al constructor, eliminant la dependència directa de EmailNotificador.
"""

# ==========================================
# CODI ORIGINAL (Alt Acoplament)
# ==========================================
"""
class EmailNotificador:
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

class Comanda:
    def __init__(self, client):
        self.client = client
        self.notificador = EmailNotificador() # Alt acoplament

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")
"""

# ==========================================
# CODI REFACTORITZAT (Baix Acoplament)
# ==========================================

class EmailNotificador:
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

class SMSNotificador:
    """Una altra implementació de notificador per demostrar flexibilitat."""
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class Comanda:
    def __init__(self, client, notificador):
        self.client = client
        # Injecció de dependència: el notificador es passa com a argument
        self.notificador = notificador 

    def confirmar(self):
        print(f"Comanda confirmada per a {self.client}")
        # Delegació de la notificació
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")

if __name__ == "__main__":
    print("--- Test amb EmailNotificador ---")
    notificador_email = EmailNotificador()
    comanda1 = Comanda("Client X", notificador_email)
    comanda1.confirmar()

    print("\n--- Test amb SMSNotificador (canvi d'implementació sense tocar Comanda) ---")
    notificador_sms = SMSNotificador()
    comanda2 = Comanda("Client Y", notificador_sms)
    comanda2.confirmar()
