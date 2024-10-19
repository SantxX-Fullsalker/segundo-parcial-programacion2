class Ventana:
    ESTILOS_VALIDOS = {"O": 1, "XO": 2, "OXO": 3, "OXXO": 4}
    ACABADOS_VALIDOS = ["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"]
    TIPOS_VIDRIO_VALIDOS = ["Transparente", "Bronce", "Azul"]

    def __init__(self, estilo, ancho, alto, acabado, tipo_vidrio, esmerilado=False):
        if estilo not in self.ESTILOS_VALIDOS:
            raise ValueError(f"Estilo de ventana '{estilo}' no es válido.")
        if acabado not in self.ACABADOS_VALIDOS:
            raise ValueError(f"Acabado '{acabado}' no es válido.")
        if tipo_vidrio not in self.TIPOS_VIDRIO_VALIDOS:
            raise ValueError(f"Tipo de vidrio '{tipo_vidrio}' no es válido.")
        
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado

        self.validar_dimensiones()

    def calcular_ancho_naves(self):
        naves = self.ESTILOS_VALIDOS[self.estilo]
        return self.ancho / naves, naves

    def calcular_area_nave(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        return (ancho_nave - 1.5) * (self.alto - 1.5)

    def calcular_perimetro_nave(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        return 2 * (ancho_nave + self.alto) - 4 * 4

    def calcular_costo_aluminio(self):
        costo_por_cm_lineal = {
            "Pulido": 50700 / 100,
            "Lacado Brillante": 54200 / 100,
            "Lacado Mate": 53600 / 100,
            "Anodizado": 57300 / 100
        }
        perimetro_total = self.calcular_perimetro_nave() * self.calcular_ancho_naves()[1]
        return perimetro_total * costo_por_cm_lineal[self.acabado]

    def calcular_costo_vidrio(self):
        costo_por_cm2 = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        area_total = self.calcular_area_nave() * self.calcular_ancho_naves()[1]
        costo_vidrio = area_total * costo_por_cm2[self.tipo_vidrio]
        if self.esmerilado:
            costo_vidrio += area_total * 5.20
        return costo_vidrio

    def calcular_costo_esquinas(self):
        return 4310 * 4

    def calcular_costo_chapa(self):
        if "X" in self.estilo:
            return 16200
        return 0

    def calcular_costo_total(self):
        return self.calcular_costo_aluminio() + self.calcular_costo_vidrio() + self.calcular_costo_esquinas() + self.calcular_costo_chapa()

    def validar_dimensiones(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        if ancho_nave <= 0 or self.alto <= 0:
            raise ValueError("Las dimensiones de la nave deben ser mayores a cero.")
        if ancho_nave <= 1.5 or self.alto <= 1.5:
            raise ValueError("Las naves no pueden ser más pequeñas que el vidrio menos los márgenes de 1.5 cm.")