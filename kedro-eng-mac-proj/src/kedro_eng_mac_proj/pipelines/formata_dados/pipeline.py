"""
This is a boilerplate pipeline 'formata_dados'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.formata_dados,
            inputs="df_dev",
            outputs="dataset_kobe_dev_formated"
        ),
        node(
            nodes.formata_dados,
            inputs="df_prod",
            outputs="dataset_kobe_prod_formated"
        )
    ])
