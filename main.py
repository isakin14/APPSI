import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet.core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "AppSI"
    page.window.width = 450
    page.window.height = 700
    page.window.resizable = False
    page.window.maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Primeiro formulário de login
    text_usuario: TextField = TextField(label='Usuario', text_align=ft.TextAlign.LEFT, width=200)
    text_senha: TextField = TextField(label='Senha', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='Concordo com tudo', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Entrar', width=200, disabled=True)
    
    # Validar Login
    def validar(e: ControlEvent) -> None:
        if all([text_usuario.value, text_senha.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
            
        page.update()


    def submit(e: ControlEvent) -> None:
        print('Usuario:', text_usuario.value)
        print('Senha:', text_senha.value)

        # Limpar a página e adicionar a tela de boas-vindas
        page.clean()

        # Tela de boas-vindas
        bem_vindo = Row(
            controls=[Text(value=f'Bem-Vindo: {text_usuario.value}', size=20)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Exibe a tela de boas-vindas
        page.add(bem_vindo)

        # Criando uma aba
        aba_em_branco = Column(
            controls=[Text(value="Esta é uma aba em branco.", size=16)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Criando as abas
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Aba em branco", content=aba_em_branco),
                ft.Tab(text="Aba em branco 2", content=aba_em_branco)  # Outra aba
            ]
        )

        # Adiciona as abas
        def add_tabs():
            page.add(tabs)
        
        # Botão para mostrar as abas após a tela inicial
        page.add(
            Row(
                controls=[ft.ElevatedButton(text="Mostrar Abas", on_click=lambda e: add_tabs())],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )  

    # Validação
    checkbox_signup.on_change = validar
    text_usuario.on_change = validar
    text_senha.on_change = validar
    button_submit.on_click = submit

    # Tela inicial (LOGIN)
    page.add(
        Row(
            controls=[Column(
                [text_usuario,
                 text_senha,
                 checkbox_signup,
                 button_submit]
            )],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
