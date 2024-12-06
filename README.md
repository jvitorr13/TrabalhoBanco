# Sistema de Banco de Dados Master/Slave

## Descrição
Simulação de um sistema de replicação Master/Slave usando Python e SQLite. O banco master permite inserções, e o slave replica os dados automaticamente.

## Arquivos Principais
- **`master.py`**: Criação e inserção de dados no banco master.
- **`slave.py`**: Replicação automática do master para o slave.
- **`check_master.py`**: Visualiza dados no master.
- **`check_slave.py`**: Visualiza dados no slave.

## Tecnologias
- **Python 3.x**
- **SQLite**

## Como Usar

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/<username>/<reponame>.git
   cd <reponame>
