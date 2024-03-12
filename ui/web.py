"""Gerar a aplicação web."""

from shiny import App, Inputs, Outputs, Session, render, ui, req
from busca.buscador import processar_textgrid

# from relatorio.relatorio_txt import gerar_relatorio
from relatorio.relatorio_oop import RelatorioGeral
from utils import abrir_arquivos_dir

app_ui = ui.page_fluid(
    ui.input_text("termo", "Busque um termo em nheengatu:", ""),
    ui.row(
        ui.column(
            6,
            ui.output_text_verbatim("saida", placeholder=True),
        ),
    ),
)

# Lista de TextGrid
textgrids_lista = abrir_arquivos_dir(".")

print(textgrids_lista)


def server(input: Inputs, output: Outputs, session: Session):

    @render.text
    def saida():

        termo_input = input.termo()
        req(input.termo())

        relatorio = RelatorioGeral()
        contador_total = 0

        for arquivo_textgrid in textgrids_lista:
            # Buscar textgrid
            contador, detalhes_ocorrencias, tg = processar_textgrid(
                arquivo_textgrid, termo_input
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

        return "".join(map(str, relatorio.conteudo))


def get_app():
    """Retorna a aplicação App."""
    app = App(app_ui, server)

    return app
