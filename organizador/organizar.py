"""
Mòdulo organizador de arquivos por extensão.

Este módulo atende aos requisitos do projeto 1 do Curso de Introdução ao Python (UFRGS/TCE-RS)

Autor:  Everton da Rosa
"""

import os
import shutil


def organizar(origem, destino, *args):
    print(f'Organizando arquivos de {origem} em {destino}')
    for extensao, diretorio in args:
        # Cria o diretório de destino se não existe
        dir_destino = os.path.abspath(os.path.join(destino, diretorio))
        criar_diretorios(dir_destino)
        # Filtra os arquivos a copiar pela extensão
        arquivos_para_copiar = filtrar_por_extensao(origem, extensao)
        # Copiando os arquivos
        for arquivo in arquivos_para_copiar:
            arq_origem = arquivo.path
            arq_destino = os.path.join(destino, diretorio, arquivo.name)
            copiar_arquivos(arq_origem, arq_destino)


def criar_diretorios(diretorio):
    print(f'Criando {diretorio}')
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)


def copiar_arquivos(origem, destino):
    print(f'Copiando {origem} para {destino}')
    shutil.copyfile(origem, destino)


def filtrar_por_extensao(origem, extensao):
    print(f'Filtrando arquivos com extensão {extensao} em {origem}')
    copiar = []
    for arquivo in os.scandir(origem):
        if arquivo.is_file() and arquivo.name.endswith(extensao):
            copiar.append(arquivo)
    return copiar
