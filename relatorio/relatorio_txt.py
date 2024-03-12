"""Anotar e gerar relatório."""


def anotar_nome_do_arquivo_e_ocorrencias(relatorio, arquivo_textgrid, contador):
    """Dados relatorio, arquivo_textgrid e contador, anota o nome do arquivo e seu número de ocorrências."""
    relatorio.append("\n\n")
    relatorio.append("---------------------------------------------")
    relatorio.append("\n")
    relatorio.append(arquivo_textgrid)
    relatorio.append("\n")
    relatorio.append("n = ")
    relatorio.append(str(contador))
    relatorio.append("\n")
    relatorio.append("---------------------------------------------")
    relatorio.append("\n\n")


def detalhar_ocorrencias(relatorio, detalhes_ocorrencias, tg):
    """Dados relatorio, detalhes_ocorrencias e tg, anota a ocorrência com base na 'The Leipzig Glossing Rules'."""
    for ocorrencia in detalhes_ocorrencias:

        indice = ocorrencia["indice"]
        camada = ocorrencia["camada"]

        prefixo_falante = "Falante1_" if camada == 0 else "Falante2_"
        inicio_anotacao = round(tg[camada][indice].minTime, 2)
        final_anotacao = round(tg[camada][indice].maxTime, 2)

        relatorio.append(prefixo_falante)
        relatorio.append(inicio_anotacao)
        relatorio.append("-")
        relatorio.append(final_anotacao)
        relatorio.append(":")
        relatorio.append("\n")

        for camada_indice in range(0, 6):

            relatorio.append(tg[camada + camada_indice][indice].mark)
            relatorio.append("\n")
        relatorio.append("\n")


def anotar_comeco_relatorio(
    relatorio, textgrids_lista, arquivo_textgrid, contador_total, termo_input
):
    """Dados relatorio, textgrids_lista, arquivo_textgrid, contador_total e termo_input,
    anota no começo do relatório o termo buscado, número de ocorrências encontradas e nome dos arquivos.
    """
    if arquivo_textgrid == textgrids_lista[len(textgrids_lista) - 1]:
        # Anotar começo do relatório
        relatorio.insert(0, f"Termo buscado = {termo_input}")
        relatorio.insert(1, "\n")
        relatorio.insert(2, "\n")
        relatorio.insert(3, f"{contador_total} ocorrências encontradas")
        relatorio.insert(4, "\n")
        relatorio.insert(5, "\n")
        relatorio.insert(6, "Arquivos")
        relatorio.insert(7, "\n")
        for i_textgrid in reversed(range(0, len(textgrids_lista))):
            relatorio.insert(8, textgrids_lista[i_textgrid])
            relatorio.insert(9, "\n")


def gerar_relatorio(
    termo_imput,
    relatorio,
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
    anotar_nome_do_arquivo_e_ocorrencias(relatorio, arquivo_textgrid, contador)
    detalhar_ocorrencias(relatorio, detalhes_ocorrencias, tg)
    anotar_comeco_relatorio(
        relatorio, textgrids_lista, arquivo_textgrid, contador_total, termo_imput
    )
