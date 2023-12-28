import flet as ft
import time

def main(page):
    nombre = ft.TextField(label="Nombre", autofocus=True)
    apellido = ft.TextField(label="Apellido")
    saludo = ft.Column()

    def clickBoton(e):
        saludo.controls.append(ft.Text(f"Hola, {nombre.value} {apellido.value}!"))
        nombre.value = ""
        apellido.value = ""
        page.update()
        nombre.focus()

    page.add(
        nombre,
        apellido,
        ft.ElevatedButton("Di Hola", on_click=clickBoton),
        saludo,
    )
ft.app(target=main)
