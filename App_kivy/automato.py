import sys
from random import sample
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton, QFrame, QVBoxLayout, QWidget, QMessageBox

regras_jogos = {
    "Mega-sena": {"min_dezenas": 6, "max_dezenas": 20, "min_valor": 1, "max_valor": 60},
    "Quina": {"min_dezenas": 5, "max_dezenas": 15, "min_valor": 1, "max_valor": 80},
    "Lotofácil": {"min_dezenas": 15, "max_dezenas": 20, "min_valor": 1, "max_valor": 25},
    "Lotomania": {"min_dezenas": 50, "max_dezenas": 50, "min_valor": 1, "max_valor": 100},
    "Timemania": {"min_dezenas": 10, "max_dezenas": 10, "min_valor": 1, "max_valor": 80}
}

class GeradorJogos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Jogos")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        label_titulo = QLabel("Gerador de Jogos", self)
        label_titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label_titulo)

        label_quantidade = QLabel("Quantidade de jogos:", self)
        layout.addWidget(label_quantidade)

        entry_jogos = QLineEdit(self)
        layout.addWidget(entry_jogos)

        label_opcao = QLabel("Escolha um jogo:", self)
        layout.addWidget(label_opcao)

        combo_opcao = QComboBox(self)
        combo_opcao.addItems(regras_jogos.keys())
        layout.addWidget(combo_opcao)

        dezenas_frame = QFrame(self)
        layout_dezenas = QVBoxLayout()
        dezenas_frame.setLayout(layout_dezenas)
        layout.addWidget(dezenas_frame)

        label_dezenas = QLabel("Escolha o número de dezenas:", self)
        layout_dezenas.addWidget(label_dezenas)

        combo_dezenas = QComboBox(self)
        layout_dezenas.addWidget(combo_dezenas)

        label_numeros_considerar = QLabel("Números a considerar (opcional):", self)
        layout.addWidget(label_numeros_considerar)

        entry_numeros_considerar = QLineEdit(self)
        layout.addWidget(entry_numeros_considerar)

        label_numeros_desconsiderar = QLabel("Números a desconsiderar (opcional):", self)
        layout.addWidget(label_numeros_desconsiderar)

        entry_numeros_desconsiderar = QLineEdit(self)
        layout.addWidget(entry_numeros_desconsiderar)

        button_gerar = QPushButton("Gerar Jogos", self)
        button_gerar.clicked.connect(self.gerar_jogos)
        layout.addWidget(button_gerar)

        resultado_text = QTextEdit(self)
        resultado_text.setReadOnly(True)
        layout.addWidget(resultado_text)

        combo_opcao.currentIndexChanged.connect(self.atualizar_opcao)

        self.dezenas_frame = dezenas_frame
        self.entry_jogos = entry_jogos
        self.combo_opcao = combo_opcao
        self.combo_dezenas = combo_dezenas
        self.entry_numeros_considerar = entry_numeros_considerar
        self.entry_numeros_desconsiderar = entry_numeros_desconsiderar
        self.resultado_text = resultado_text

        self.atualizar_opcao()

    def atualizar_opcao(self):
        opcao = self.combo_opcao.currentText()

        if opcao in ["Lotomania", "Timemania"]:
            self.dezenas_frame.hide()
        else:
            self.dezenas_frame.show()

            self.combo_dezenas.clear()
            for i in range(regras_jogos[opcao]['min_dezenas'], regras_jogos[opcao]['max_dezenas'] + 1):
                self.combo_dezenas.addItem(str(i))
            self.combo_dezenas.setCurrentText(str(regras_jogos[opcao]['min_dezenas']))

    def gerar_jogos(self):
        opcao = self.combo_opcao.currentText()
        jogos_solicitados = self.entry_jogos.text()
        dezenas_solicitadas = int(self.combo_dezenas.currentText()) if self.dezenas_frame.isVisible() else regras_jogos[opcao]["min_dezenas"]
        numeros_considerar = self.entry_numeros_considerar.text().split(",")
        numeros_desconsiderar = self.entry_numeros_desconsiderar.text().split(",")

        if not jogos_solicitados.isdigit():
            QMessageBox.critical(self, "Erro", "Quantidade de jogos inválido!")
            return

        jogos_solicitados = int(jogos_solicitados)

        if not regras_jogos[opcao]["min_dezenas"] <= dezenas_solicitadas <= regras_jogos[opcao]["max_dezenas"]:
            QMessageBox.critical(self, "Erro", "Número de dezenas inválido!")
            return

        self.resultado_text.clear()

        numeros_considerar = [int(num) for num in numeros_considerar if num.strip().isdigit()]
        numeros_desconsiderar = [int(num) for num in numeros_desconsiderar if num.strip().isdigit()]

        if opcao == "Lotofácil" and any(num > regras_jogos[opcao]["max_valor"] for num in numeros_considerar):
            QMessageBox.critical(self, "Erro", "Valor inválido para o jogo Lotofácil!")
            return

        if any(num > 99 for num in numeros_considerar + numeros_desconsiderar):
            QMessageBox.critical(self, "Erro", "Valor inválido! Apenas números de 1 a 99 são permitidos.")
            return

        jogos_gerados = 0
        tentativas = 0

        while jogos_gerados < jogos_solicitados:
            tentativas += 1
            jogo = sorted(sample(range(regras_jogos[opcao]["min_valor"], regras_jogos[opcao]["max_valor"] + 1), dezenas_solicitadas))

            if all(num in jogo for num in numeros_considerar) and all(num not in jogo for num in numeros_desconsiderar):
                jogos_gerados += 1

                self.resultado_text.append(f"<b>{jogos_gerados}° Jogo:</b>")
                self.resultado_text.append(" _ ".join(f"<u>{dezena}</u>" for dezena in jogo))
                self.resultado_text.append("")  # Adiciona uma linha em branco após cada jogo

            if tentativas >= 100000:
                QMessageBox.warning(self, "Aviso", "Não foi possível gerar a quantidade de jogos solicitada com as restrições especificadas.")
                break

app = QApplication(sys.argv)
janela = GeradorJogos()
janela.show()
sys.exit(app.exec_())
