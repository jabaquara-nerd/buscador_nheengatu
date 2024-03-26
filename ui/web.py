"""Gerar a aplicação web."""

from shiny import App, Inputs, Outputs, Session, render, ui, req, reactive
from busca.buscador import processar_textgrid

# from relatorio.relatorio_txt import gerar_relatorio
from relatorio.relatorio_oop import RelatorioGeral, RelatorioSimples
from utils import abrir_arquivos_dir


app_ui = ui.page_fluid(
    ui.input_text("termo", "Digite o termo a ser buscado:", ""),
    ui.input_radio_buttons(
        "camada_buscada",
        "Buscar em:",
        {"nheengatu": "Nheengatu", "portugues": "Português", "glosa": "Glosa"},
    ),
    ui.input_radio_buttons(
        "select",
        "Selecione o tipo do relatório:",
        {"simples": "Simples", "completo": "Completo"},
    ),
    ui.row(
        ui.column(
            6,
            ui.output_text_verbatim("saida"),
        ),
    ),
)


# Lista de TextGrid
textgrids_lista = abrir_arquivos_dir(".")


def server(input: Inputs, output: Outputs, session: Session):

    @render.text
    def saida():

        req(input.termo(), cancel_output=True)

        req(input.camada_buscada())

        termo_input = input.termo()

        camada_buscada_input = input.camada_buscada()

        contador_total = 0

        tipo_relatorio_input = input.select()

        if tipo_relatorio_input == "completo":
            relatorio = RelatorioGeral()
        else:
            relatorio = RelatorioSimples()

        for arquivo_textgrid in textgrids_lista:
            # Buscar textgrid
            contador, detalhes_ocorrencias, tg = processar_textgrid(
                arquivo_textgrid, termo_input, camada_buscada_input
            )

            # Atualizar os contadores
            contador_total = contador_total + contador

            relatorio.gerar_relatorio(
                termo_input,
                arquivo_textgrid,
                contador,
                detalhes_ocorrencias,
                tg,
                textgrids_lista,
                contador_total,
            )

        def printar_relatorio():

            saida_relatorio = "".join(map(str, relatorio.conteudo))
            RelatorioGeral.conteudo = []

            return saida_relatorio

        return printar_relatorio()


def get_app():
    """Retorna a aplicação App."""
    app = App(app_ui, server)

    return app
