"""Processar e extrair as ocorrências."""

from unidecode import unidecode
import textgrid

# Definir camada de falantes
FALANTE_1_TIER_1 = 0
FALANTE_2_TIER_1 = 6


def busca_termo_corpus_total(termo_buscado, corpus_total):
    """Dados termo_buscado e corpus_total, busca o termo em todos os arquivos do corpus."""
    contador = 0
    termo_limpo = unidecode(termo_buscado.upper())
    detalhes_ocorrencias = []

    for item in corpus_total:
        foi_encontrado = termo_limpo in unidecode(item["text"].upper())
        if foi_encontrado:
            local = {"indice": item["indice"], "camada": item["camada"]}
            detalhes_ocorrencias.append(local)
            contador += 1

    return contador, detalhes_ocorrencias


def processar_textgrid(arquivo_textgrid, termo_input):
    """Dados arquivo_textgrid, termo_input, processa o TextGrid."""

    tg = textgrid.TextGrid.fromFile(arquivo_textgrid)

    corpus_falante_1 = extrair_corpus_falante(FALANTE_1_TIER_1, tg)
    corpus_falante_2 = extrair_corpus_falante(FALANTE_2_TIER_1, tg)
    corpus_falantes_total = corpus_falante_1 + corpus_falante_2

    # Buscar textgrid
    contador, detalhes_ocorrencias = busca_termo_corpus_total(
        termo_input, corpus_falantes_total
    )

    return contador, detalhes_ocorrencias, tg


def extrair_corpus_falante(camada_falante, tg):
    """Dados camada_falante, tg, extrai anotações do TextGrid."""
    ultimo_indice = len(tg[camada_falante])
    corpus_falante = []

    # Alguns TextGrids tem apenas 1 falante e 6 camadas.
    if len(tg) > 10:
        for indice in range(0, ultimo_indice):
            intervalo = tg[camada_falante][indice]
            is_empty = intervalo.mark == ""
            if not is_empty:
                item = {
                    "text": intervalo.mark,
                    "indice": indice,
                    "camada": camada_falante,
                }
                corpus_falante.append(item)

    return corpus_falante
