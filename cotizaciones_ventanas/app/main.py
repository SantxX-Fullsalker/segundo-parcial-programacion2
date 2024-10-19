from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente

console = Console()

def mostrar_menu():
    console.print("[bold cyan]Sistema de Cotización de Ventanas[/bold cyan]", justify="center")
    console.print("[bold green]1.[/bold green] Crear cotización")
    console.print("[bold red]2.[/bold red] Salir")

def seleccionar_opcion(mensaje, opciones):
    console.print(mensaje)
    for i, opcion in enumerate(opciones, 1):
        console.print(f"{i}. {opcion}")
    seleccion = int(Prompt.ask("Ingrese el número de la opción"))
    if 1 <= seleccion <= len(opciones):
        return opciones[seleccion - 1]
    else:
        raise ValueError("Opción inválida.")

def crear_cotizacion():
    nombre_cliente = Prompt.ask("[bold yellow]Ingrese el nombre del cliente[/bold yellow]")
    empresa_cliente = Prompt.ask("[bold yellow]Ingrese el nombre de la empresa[/bold yellow]")
    cantidad_ventanas = int(Prompt.ask("[bold yellow]Ingrese la cantidad de ventanas[/bold yellow]"))
    cliente = Cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)

    ventanas = []
    for _ in range(cantidad_ventanas):
        estilo = seleccionar_opcion("[bold cyan]Seleccione el estilo de la ventana:[/bold cyan]", ["O", "XO", "OXXO", "OXO"])
        ancho = float(Prompt.ask("[bold cyan]Ingrese el ancho de la ventana (cm)[/bold cyan]"))
        alto = float(Prompt.ask("[bold cyan]Ingrese el alto de la ventana (cm)[/bold cyan]"))
        acabado = seleccionar_opcion("[bold cyan]Seleccione el tipo de acabado:[/bold cyan]", 
                                     ["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"])
        tipo_vidrio = seleccionar_opcion("[bold cyan]Seleccione el tipo de vidrio:[/bold cyan]", 
                                         ["Transparente", "Bronce", "Azul"])
        esmerilado = seleccionar_opcion("[bold cyan]Esmerilado?[/bold cyan]", ["Sí", "No"]).lower() == "sí"
        
        ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)
        ventanas.append(ventana)

    cotizacion = Cotizacion(cliente, ventanas)
    total = cotizacion.calcular_total()

    # Crear tabla para mostrar el resumen de la cotización
    table = Table(title="Resumen de Cotización")

    table.add_column("Cliente", style="bold cyan")
    table.add_column("Empresa", style="bold cyan")
    table.add_column("Cantidad de Ventanas", justify="right", style="bold cyan")
    table.add_column("Costo Total", justify="right", style="bold green")

    table.add_row(nombre_cliente, empresa_cliente, str(cantidad_ventanas), f"${total:.0f}")

    # Mostrar la tabla en consola
    console.print(table)
    console.print(f"[bold yellow]El costo total de la cotización es: [bold green]${total:.0f}[/bold green][/bold yellow]")

def main():
    while True:
        
        mostrar_menu()
        opcion = Prompt.ask("[bold blue]Seleccione una opción[/bold blue]")
        if opcion == '1':
            crear_cotizacion()
        elif opcion == '2':
            console.print("[bold red]Saliendo...[/bold red]")
            break
        else:
            console.print("[bold red]Opción inválida. Intente de nuevo.[/bold red]")

if __name__ == "__main__":
    main()
