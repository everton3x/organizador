"""
Ponto de entrada do programa organizador.

Autor:  Everton da Rosa
e-mail: contabilidade@independencia.rs.gov.br
"""

from organizador import organizar

def main():
    dir_documentos = 'documentos'
    dir_planilhas = 'planilhas'
    origem = r'../intprogpython/projeto1/'
    destino = r'./arquivos_organizados/'
    organizar.organizar(
        origem,
        destino,
        ('.doc', dir_documentos),
        ('.xls', dir_planilhas),
        ('.docx', dir_documentos),
        ('.xls', dir_planilhas),
        ('.doc', dir_documentos)
    )

if __name__ == "__main__":
    main()