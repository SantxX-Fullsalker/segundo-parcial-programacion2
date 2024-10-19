import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ventana import Ventana
from app.cotizacion import Cotizacion
from app.cliente import Cliente

# Test para la clase Ventana
def test_calcular_ancho_naves():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    ancho_nave, naves = ventana.calcular_ancho_naves()
    assert ancho_nave == 60
    assert naves == 2

def test_calcular_area_nave():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    area_nave = ventana.calcular_area_nave()
    assert area_nave == (60 - 1.5) * (100 - 1.5)

def test_calcular_perimetro_nave():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    perimetro_nave = ventana.calcular_perimetro_nave()
    assert perimetro_nave == 2 * (60 + 100) - 4 * 4

def test_calcular_costo_aluminio():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    costo_aluminio = ventana.calcular_costo_aluminio()
    assert costo_aluminio == ventana.calcular_perimetro_nave() * 2 * (50700 / 100)

def test_calcular_costo_vidrio():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    costo_vidrio = ventana.calcular_costo_vidrio()
    assert costo_vidrio == ventana.calcular_area_nave() * 2 * 8.25

def test_calcular_costo_esquinas():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    costo_esquinas = ventana.calcular_costo_esquinas()
    assert costo_esquinas == 4310 * 4

def test_calcular_costo_chapa():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    costo_chapa = ventana.calcular_costo_chapa()
    assert costo_chapa == 16200

def test_calcular_costo_total():
    ventana = Ventana("XO", 120, 100, "Pulido", "Transparente")
    costo_total = ventana.calcular_costo_total()
    assert costo_total == (
        ventana.calcular_costo_aluminio() +
        ventana.calcular_costo_vidrio() +
        ventana.calcular_costo_esquinas() +
        ventana.calcular_costo_chapa()
    )

# Test para la clase Cotizacion
def test_calcular_total_cotizacion_sin_descuento():
    cliente = Cliente("Cliente 1", "Empresa", 50)
    ventanas = [Ventana("XO", 120, 100, "Pulido", "Transparente") for _ in range(50)]
    cotizacion = Cotizacion(cliente, ventanas)
    total = cotizacion.calcular_total()
    expected_total = sum(ventana.calcular_costo_total() for ventana in ventanas)
    assert total == expected_total

def test_calcular_total_cotizacion_con_descuento():
    cliente = Cliente("Cliente 2", "Empresa", 150)
    ventanas = [Ventana("XO", 120, 100, "Pulido", "Transparente") for _ in range(150)]
    cotizacion = Cotizacion(cliente, ventanas)
    total = cotizacion.calcular_total()
    expected_total = sum(ventana.calcular_costo_total() for ventana in ventanas) * 0.9
    assert total == expected_total

