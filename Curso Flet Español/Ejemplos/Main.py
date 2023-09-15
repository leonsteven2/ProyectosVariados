import flet
from flet import Page, Row, Column, ElevatedButton, TextField, IconButton, icons, Text


def main(page: Page):
    page.add(
        Row(controls=[
            TextField(hint_text="Escriba aquí"),
            IconButton(icons.SEARCH)
        ], alignment="center"
        ),
        Column(controls=[
            Text("Asd")
        ]),
        Column(controls=[
            Text("Asd")
        ]),
    )


flet.app(target=main)
