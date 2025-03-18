"""
Formatar os dados do kobe
"""

def formata_dados(base):
    # Aplicar transformações e limpeza necessárias
    base.dropna(subset=['shot_made_flag'], inplace=True)
    return base