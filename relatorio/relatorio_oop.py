class RelatorioGeral:

    conteudo = []

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

        self._anotar_nome_do_arquivo_e_ocorrencias(arquivo_textgrid, contador)

        self._detalhar_ocorrencias(detalhes_ocorrencias, tg)

        self._anotar_comeco_relatorio(
            textgrids_lista, arquivo_textgrid, contador_total, termo_input
        )

    def _anotar_nome_do_arquivo_e_ocorrencias(self, arquivo_textgrid, contador):
        """Dados relatorio, arquivo_textgrid e contador, anota o nome do arquivo e seu número de ocorrências."""

        self.conteudo.append("\n\n")
        self.conteudo.append("---------------------------------------------")
        self.conteudo.append("\n")
        self.conteudo.append(arquivo_textgrid)
        self.conteudo.append("\n")
        self.conteudo.append("n = ")
        self.conteudo.append(str(contador))
        self.conteudo.append("\n")
        self.conteudo.append("---------------------------------------------")
        self.conteudo.append("\n\n")

    def _detalhar_ocorrencias(self, detalhes_ocorrencias, tg):
        """Dados relatorio, detalhes_ocorrencias e tg, anota a ocorrência com base na 'The Leipzig Glossing Rules'."""
        for ocorrencia in detalhes_ocorrencias:

            indice = ocorrencia["indice"]
            camada = ocorrencia["camada"]

            prefixo_falante = "Falante1_" if camada == 0 else "Falante2_"
            inicio_anotacao = round(tg[camada][indice].minTime, 2)
            final_anotacao = round(tg[camada][indice].maxTime, 2)

            self.conteudo.append(prefixo_falante)
            self.conteudo.append(inicio_anotacao)
            self.conteudo.append("-")
            self.conteudo.append(final_anotacao)
            self.conteudo.append(":")
            self.conteudo.append("\n")

            for camada_indice in range(0, 6):

                self.conteudo.append(tg[camada + camada_indice][indice].mark)
                self.conteudo.append("\n")
            self.conteudo.append("\n")

    def _anotar_comeco_relatorio(
        self, textgrids_lista, arquivo_textgrid, contador_total, termo_input
    ):
        """Dados relatorio, textgrids_lista, arquivo_textgrid, contador_total e termo_input,
        anota no começo do relatório o termo buscado, número de ocorrências encontradas e nome dos arquivos.
        """
        if arquivo_textgrid == textgrids_lista[len(textgrids_lista) - 1]:
            # Anotar começo do relatório
            self.conteudo.insert(0, "Relatório completo\n")
            self.conteudo.insert(1, "\n")
            self.conteudo.insert(2, f"Termo buscado = {termo_input}\n\n")
            self.conteudo.insert(3, f"{contador_total} ocorrências encontradas")
            self.conteudo.insert(4, "\n")
            self.conteudo.insert(5, "\n")
            self.conteudo.insert(6, "Arquivos")
            self.conteudo.insert(7, "\n")
            for i_textgrid in reversed(range(0, len(textgrids_lista))):
                self.conteudo.insert(8, textgrids_lista[i_textgrid])
                self.conteudo.insert(9, "\n")


class RelatorioSimples(RelatorioGeral):

    def _detalhar_ocorrencias(self, detalhes_ocorrencias, tg):
        """Dados relatorio, detalhes_ocorrencias e tg, anota a ocorrência com base na 'The Leipzig Glossing Rules'."""
        for ocorrencia in detalhes_ocorrencias:

            indice = ocorrencia["indice"]
            camada = ocorrencia["camada"]

            for camada_indice in 0, 2, 4:

                self.conteudo.append(tg[camada + camada_indice][indice].mark)
                self.conteudo.append("\n")
            self.conteudo.append("\n")

    def _anotar_comeco_relatorio(
        self, textgrids_lista, arquivo_textgrid, contador_total, termo_input
    ):
        """Dados relatorio, textgrids_lista, arquivo_textgrid, contador_total e termo_input,
        anota no começo do relatório o termo buscado, número de ocorrências encontradas e nome dos arquivos.
        """
        if arquivo_textgrid == textgrids_lista[len(textgrids_lista) - 1]:
            # Anotar começo do relatório
            self.conteudo.insert(0, "Relatório simples")
            self.conteudo.insert(1, "\n\n")
            self.conteudo.insert(2, f"Termo buscado = {termo_input}\n\n")
            self.conteudo.insert(3, f"{contador_total} ocorrências encontradas")
