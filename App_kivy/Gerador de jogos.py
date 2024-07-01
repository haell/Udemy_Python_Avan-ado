from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from random import sample

regras_jogos = {
    "Mega-sena": {"min_dezenas": 6, "max_dezenas": 20, "min_valor": 1, "max_valor": 60},
    "Quina": {"min_dezenas": 5, "max_dezenas": 15, "min_valor": 1, "max_valor": 80},
    "Lotofácil": {"min_dezenas": 15, "max_dezenas": 20, "min_valor": 1, "max_valor": 25},
    "Lotomania": {"min_dezenas": 50, "max_dezenas": 50, "min_valor": 1, "max_valor": 100},
    "Timemania": {"min_dezenas": 10, "max_dezenas": 10, "min_valor": 1, "max_valor": 80}
}

class GeradorJogosApp(App):
    def build(self):
        self.title = "Gera loteria"
        layout = GridLayout(cols=1, spacing=10, padding=10)
        
        # Linha 1
        label_titulo = Label(text="Gerador de Jogos HAELLTEC", font_size=16, bold=True, halign='center', valign='middle', size_hint=(1, 0.1))
        layout.add_widget(label_titulo)

        # Subgrid para as linhas 2 a 6
        subgrid = GridLayout(cols=4, spacing=10)

        # Linha 2 - Quantidade de jogos com incremento e decremento
        subgrid.add_widget(Label())  # Coluna 1 vazia
        subgrid.add_widget(Label(text="Quantidade de jogos:", height=40, size_hint_y=None))  # Coluna 2
        quantidade_layout = GridLayout(cols=3, size_hint=(1, None), height=40)
        self.entry_jogos = TextInput(text='1', height=40, size_hint_y=None, multiline=False)
        self.entry_jogos.bind(text=self.validate_jogos_input)
        btn_decrementar = Button(text='-', height=40, size_hint_y=None)
        btn_decrementar.bind(on_press=self.decrementar_jogos)
        btn_incrementar = Button(text='+', height=40, size_hint_y=None)
        btn_incrementar.bind(on_press=self.incrementar_jogos)
        quantidade_layout.add_widget(btn_decrementar)
        quantidade_layout.add_widget(self.entry_jogos)
        quantidade_layout.add_widget(btn_incrementar)
        subgrid.add_widget(quantidade_layout)  # Coluna 3
        subgrid.add_widget(Label())  # Coluna 4 vazia

        # Linha 3 - Escolha de jogo
        subgrid.add_widget(Label())  # Coluna 1 vazia
        subgrid.add_widget(Label(text="Escolha um jogo:", height=40, size_hint_y=None))  # Coluna 2
        self.combo_opcao = Spinner(
            text='Mega-sena',
            values=list(regras_jogos.keys()),
            height=40,
            size_hint_y=None
        )
        self.combo_opcao.bind(text=self.atualizar_opcao)
        subgrid.add_widget(self.combo_opcao)  # Coluna 3
        subgrid.add_widget(Label())  # Coluna 4 vazia

        # Linha 4 - Escolha do número de dezenas
        subgrid.add_widget(Label())  # Coluna 1 vazia
        self.label_dezenas = Label(text="Escolha o número de dezenas:", height=40, size_hint_y=None)
        subgrid.add_widget(self.label_dezenas)  # Coluna 2
        self.combo_dezenas = Spinner(height=40, size_hint_y=None)
        subgrid.add_widget(self.combo_dezenas)  # Coluna 3
        subgrid.add_widget(Label())  # Coluna 4 vazia

        # Linha 5 - Números a considerar
        subgrid.add_widget(Label())  # Coluna 1 vazia
        subgrid.add_widget(Label(text="Números a considerar:", height=40, size_hint_y=None))  # Coluna 2
        self.entry_numeros_considerar = TextInput(height=40, size_hint_y=None)
        subgrid.add_widget(self.entry_numeros_considerar)  # Coluna 3
        subgrid.add_widget(Label())  # Coluna 4 vazia

        # Linha 6 - Números a desconsiderar
        subgrid.add_widget(Label())  # Coluna 1 vazia
        subgrid.add_widget(Label(text="Números a desconsiderar:", height=40, size_hint_y=None))  # Coluna 2
        self.entry_numeros_desconsiderar = TextInput(height=40, size_hint_y=None)
        subgrid.add_widget(self.entry_numeros_desconsiderar)  # Coluna 3
        subgrid.add_widget(Label())  # Coluna 4 vazia

        layout.add_widget(subgrid)

        # Linha 7 - Botão para gerar jogos
        button_gerar = Button(text="Gerar Jogos", size_hint=(1, None), height=40)
        layout.add_widget(button_gerar)
        button_gerar.bind(on_press=self.gerar_jogos)

        # Linha 8 - Área de resultado em ScrollView
        self.scroll_view = ScrollView(size_hint=(1, 0.6))
        self.resultado_text = Label(text='', halign='center', valign='top', size_hint_y=None)
        self.resultado_text.bind(texture_size=self.resultado_text.setter('size'))
        self.scroll_view.add_widget(self.resultado_text)
        layout.add_widget(self.scroll_view)

        self.atualizar_opcao(self.combo_opcao, self.combo_opcao.text)
        return layout

    def atualizar_opcao(self, spinner, text):
        opcao = self.combo_opcao.text
        if opcao in ["Lotomania", "Timemania"]:
            self.label_dezenas.opacity = 0
            self.combo_dezenas.opacity = 0
        else:
            self.label_dezenas.opacity = 1
            self.combo_dezenas.opacity = 1
            self.combo_dezenas.values = [str(i) for i in range(regras_jogos[opcao]['min_dezenas'], regras_jogos[opcao]['max_dezenas'] + 1)]
            self.combo_dezenas.text = str(regras_jogos[opcao]['min_dezenas'])

    def incrementar_jogos(self, instance):
        valor = int(self.entry_jogos.text)
        if valor < 100:
            valor += 1
            self.entry_jogos.text = str(valor)

    def decrementar_jogos(self, instance):
        valor = int(self.entry_jogos.text)
        if valor > 1:
            valor -= 1
            self.entry_jogos.text = str(valor)

    def validate_jogos_input(self, instance, value):
        if not value.isdigit() or int(value) < 1:
            self.entry_jogos.text = '1'
        elif int(value) > 100:
            self.entry_jogos.text = '500'

    def gerar_jogos(self, instance):
        opcao = self.combo_opcao.text
        jogos_solicitados = int(self.entry_jogos.text)
        dezenas_solicitadas = int(self.combo_dezenas.text) if self.combo_dezenas.opacity == 1 else regras_jogos[opcao]["min_dezenas"]
        numeros_considerar = self.entry_numeros_considerar.text.split(",")
        numeros_desconsiderar = self.entry_numeros_desconsiderar.text.split(",")

        if not regras_jogos[opcao]["min_dezenas"] <= dezenas_solicitadas <= regras_jogos[opcao]["max_dezenas"]:
            self.show_popup("Erro", "Número de dezenas inválido!")
            return

        self.resultado_text.text = ""

        numeros_considerar = [int(num) for num in numeros_considerar if num.strip().isdigit()]
        numeros_desconsiderar = [int(num) for num in numeros_desconsiderar if num.strip().isdigit()]

        if opcao == "Lotofácil" and any(num > regras_jogos[opcao]["max_valor"] for num in numeros_considerar):
            self.show_popup("Erro", "Valor inválido para o jogo Lotofácil!")
            return

        if any(num > 99 for num in numeros_considerar + numeros_desconsiderar):
            self.show_popup("Erro", "Valor inválido! Apenas números de 1 a 99 são permitidos.")
            return

        jogos_gerados = set()
        tentativas = 0

        while len(jogos_gerados) < jogos_solicitados:
            tentativas += 1
            jogo = sorted(sample(range(regras_jogos[opcao]["min_valor"], regras_jogos[opcao]["max_valor"] + 1), dezenas_solicitadas))

            if all(num in jogo for num in numeros_considerar) and all(num not in jogo for num in numeros_desconsiderar):
                jogos_gerados.add(tuple(jogo))

            if tentativas >= 100000:
                self.show_popup("Aviso", "Não foi possível gerar a quantidade de jogos solicitada com as restrições especificadas.")
                break

        # Exibindo os jogos gerados
        for idx, jogo in enumerate(jogos_gerados):
            jogo_formatado = ' - '.join(f'{num:02}' if num < 10 else f'{num}' for num in jogo)
            self.resultado_text.text += f"{idx + 1}° Jogo: {jogo_formatado}\n"

        # Atualiza o tamanho do Label para caber todo o texto gerado
        self.resultado_text.height = self.resultado_text.texture_size[1]

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 400))
        popup.open()

if __name__ == '__main__':
    GeradorJogosApp().run()
