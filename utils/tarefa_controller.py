from loguru import logger
from models.tarefa_model import Tarefa
from datetime import date, datetime

class TarefaController:

    def visualizar_tarefas(self):
        for tarefa in Tarefa.select():
            logger.debug('-'*30)
            logger.debug(tarefa.nome)
            logger.debug(tarefa.descricao)
            logger.debug(tarefa.data_inicio)
            logger.debug(tarefa.data_fim)
            logger.debug(tarefa.prioridade)
            logger.debug(tarefa.status)
            logger.debug(tarefa.responsavel)

    def incluir_tarefa(self, nome:str, descricao:str, data_inicio:datetime, data_fim:date, prioridade:int, status:str, responsavel:str):
        """Incluir tarefa

        Args:
            nome (str): nome da tarefa
            descricao (str): descrição da tarefa
            data_inicio (date): data de início da tarefa
            data_fim (date): data do fim da tarefa
            prioridade (int): prioridade da tarefa,
                numérico: 1, 2, 3
            status (str): "pendente, concluida, cancelada"
            responsavel (str): nome do usuário que criou
        """
        Tarefa.create(nome=nome, descricao=descricao,
                        data_inicio = data_inicio, data_fim = data_fim,
                        prioridade=prioridade, status = status,
                        responsavel = responsavel)

if __name__ == "__main__":
    TarefaController().visualizar_tarefas()