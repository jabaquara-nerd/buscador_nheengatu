"""Anotação e produção do relatório com jinja"""

from jinja2 import Environment, PackageLoader, select_autoescape


class RelatorioTemplate:

    conteudo = ""

    def gerar_relatorio(
        self,
        termo_input,
        arquivo_textgrid,
        contador,
        detalhes_ocorrencias,
        tg,
        textgrids_lista,
        contador_total,
    ):
        """Dados

        termo_imput,
        relatorio,
        arquivo_textgrid,
        contador,
        detalhes_ocorrencias,
        tg,
        textgrids_lista,
        contador_total,

        gera o relatório."""

        dados_comeco = self._anotar_comeco_relatorio(
            textgrids_lista, arquivo_textgrid, contador_total, termo_input
        )

        env = Environment(
            loader=PackageLoader("relatorio"), autoescape=select_autoescape()
        )
        template = env.get_template("base.jinja")
        self.conteudo = template.render(comeco=dados_comeco)

    def _anotar_comeco_relatorio(
        self, textgrids_lista, arquivo_textgrid, contador_total, termo_input
    ):
        """Dados relatorio, textgrids_lista, arquivo_textgrid, contador_total e termo_input,
        anota no começo do relatório o termo buscado, número de ocorrências encontradas e nome dos arquivos.
        """
        if arquivo_textgrid == textgrids_lista[len(textgrids_lista) - 1]:
            # Anotar começo do relatório
            lista_reversa_arq_tg = reversed(textgrids_lista)
            return {
                "termo_input": termo_input,
                "contador_total": contador_total,
                "lista_reversa_arq_tg": lista_reversa_arq_tg,
            }
