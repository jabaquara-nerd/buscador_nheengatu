"""Utilitários."""

import os


def abrir_arquivos_dir(nome_diretorio):
    """Dado nome_diretorio, retorna todos os arquivos .TextGrid."""
    resultado = [
        arquivo
        for arquivo in os.listdir(nome_diretorio)
        if arquivo.endswith(".TextGrid")
    ]

    return resultado
