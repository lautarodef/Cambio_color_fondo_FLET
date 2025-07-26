import flet as ft

def main(page: ft.Page):
    contenido = ft.Text("Pestaña 1", size=25)

    def cambiar_tab(e):
        contenido.value = f"Pestaña {e.control.data}"
        page.update()

    sidebar = ft.Column([
        ft.ElevatedButton("Tab 1", on_click=cambiar_tab, data=1),
        ft.ElevatedButton("Tab 2", on_click=cambiar_tab, data=2),
        ft.ElevatedButton("Tab 3", on_click=cambiar_tab, data=3),
    ], width=150)

    page.add(
        ft.Row([
            sidebar,
            ft.Container(content=contenido, expand=True, padding=20),
        ])
    )

ft.app(target=main)
