# Estrutura simples de coleção 

|           |             **List**            |           **Tuple**           |               **Set**              |             **Dict**             |
|-----------|:---------------------------:|:-------------------------:|:------------------------------:|:----------------------------:|
| Desc.     | Sequência de valor mutaveis | Sequência fixa de valores | Sequência de valores distintos | Coleção de pares chave-valor |
| Repres.   |          [a, b, c]          |         (a, b, c)         |            {a, b, c}           |        {'a':b, 'c':d}        |
| Duplicate |             Yes             |            Yes            |               No               |       No duplicate key       |
| Ordered   |             Yes             |            Yes            |               No               |              Yes             |
| Create    |            list()           |          tuple()          |              set()             |            dict()            |

Listas e Tuplas, ao contrário de sets, podem ter valores duplicados.
Sets se assemelham a conjuntos matemáticos.

## Classe Collection
Tenho a classe `collection` que oferece mais opções de coleção.

- **Tuplas nomeadas**: Tupla com campos nomeados
- **OrderedDict**: Dicionário com propriedade especiais
- **Counter**: Contador de valores distintos
- **Deque**: Lista Encadeada


