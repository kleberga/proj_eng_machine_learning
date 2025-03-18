"""
Pipeline de carga e descrição de dados
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.download_data,
            inputs=[],
            outputs=["df_dev", "df_prod"]
        ),
        node(
            nodes.descricao_dados,
            inputs="df_dev",
            outputs="df_explorado_dev"
        ),
        node(
            nodes.descricao_dados,
            inputs="df_prod",
            outputs="df_explorado_prod"
        )
    ])
