import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet.core.control_event import ControlEvent

def main(page:ft.Page) -> None:
    page.theme_mode=ft.ThemeMode.LIGHT
    page.title="AppSI"
    page.window.width=450
    page.window.height=700
    page.window.resizable=False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_usuario: TextField = TextField(label='Usuario', text_align=ft.TextAlign.LEFT, width=200)
    text_senha: TextField = TextField(label='Senha', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='Concordo com tudo', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Entrar', width=200, disabled=True)

    def validar(e: ControlEvent) -> None:
        if all([text_usuario.value, text_usuario.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()


    def submit(e: ControlEvent) -> None:
        print('Usuario:', text_usuario.value)
        print('Senha:', text_senha.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Bem-Vindo: {text_usuario.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    checkbox_signup.on_change = validar
    text_usuario.on_change = validar
    text_usuario.on_change = validar
    button_submit.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    [text_usuario,
                     text_senha,
                     checkbox_signup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)