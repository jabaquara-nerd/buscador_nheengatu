"""Gerador da aplicação web."""

from shiny import App, Inputs, Outputs, Session, render, ui, req, reactive
from busca.buscador import processar_textgrid

# from relatorio.relatorio_txt import gerar_relatorio
from relatorio.relatorio_oop import RelatorioGeral, RelatorioSimples
from relatorio.relatorio_template import RelatorioTemplate
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
        {"simples": "Simples", "completo": "Completo", "template": "Template"},
    ),
    ui.row(
        ui.column(
            6,
            # ui.output_text_verbatim("saida"),
            ui.output_ui("saida"),
        ),
    ),
)


# Lista de TextGrid
textgrids_lista = abrir_arquivos_dir(".")


def server(input: Inputs, output: Outputs, session: Session):

    # @render.text
    #
    # @reactive.event(input.add)

    @render.ui
    def saida():

        req(input.termo(), cancel_output=True)

        req(input.camada_buscada())

        termo_input = input.termo()

        camada_buscada_input = input.camada_buscada()

        contador_total = 0

        tipo_relatorio_input = input.select()

        if tipo_relatorio_input == "completo":
            relatorio = RelatorioGeral()
        elif tipo_relatorio_input == "template":
            relatorio = RelatorioTemplate()
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
            if tipo_relatorio_input == "template":
                saida_relatorio = relatorio.conteudo
                return ui.TagList(ui.HTML(saida_relatorio))
            else:
                saida_relatorio = "".join(map(str, relatorio.conteudo))
                RelatorioGeral.conteudo = []
                # return ui.TagList(ui.output_text_verbatim(saida_relatorio))
                return ui.TagList(ui.HTML(saida_relatorio.replace("\n", "<br>")))

        return printar_relatorio()


def get_app():
    """Retorna a aplicação App."""
    app = App(app_ui, server)

    return app
