# Trabalho Prático — Divisão e Conquista

Projeto em Python com os dois problemas pedidos no enunciado.

## Requisitos
- Python 3.9 ou superior.
- Nenhuma biblioteca externa é necessária para executar algoritmos e testes.

## Arquivos
- `algoritmos.py`: força bruta, divisão e conquista e Kadane.
- `main.py`: interface simples por linha de comando.
- `tests/test_algoritmos.py`: testes automatizados.
- `casos_de_teste.json`: casos e saídas esperadas.
- `gerar_medicoes.py`: executa benchmarks e gera CSV e gráficos.
- `dados/medicoes.csv`: medições geradas nesta execução; devem ser refeitas na máquina usada no relatório.
- `relatorio.pdf`: relatório inicial com metodologia e medições desta execução.

## Executar exemplos
```bash
python main.py soma --metodo divisao-conquista --entrada exemplo_soma.json
python main.py pontos --metodo divisao-conquista --entrada exemplo_pontos.json
```
Os arquivos JSON de entrada devem seguir:
```json
{"vetor": [-2, 1, -3, 4, -1, 2, 1]}
```
ou
```json
{"pontos": [[0, 0], [3, 4], [1, 1]]}
```

## Executar testes
Na pasta do projeto:
```bash
python -m unittest discover -s tests -v
```

## Gerar novamente as medições e gráficos
```bash
python gerar_medicoes.py
```
O script realiza pelo menos cinco execuções por tamanho e grava CSV e PNGs na pasta `dados/`.

## Complexidades esperadas
| Problema | Algoritmo | Complexidade |
|---|---|---|
| Subarranjo máximo | Força bruta | O(n²) |
| Subarranjo máximo | Divisão e conquista | O(n log n) |
| Subarranjo máximo | Kadane (desafio) | O(n) |
| Par mais próximo | Força bruta | O(n²) |
| Par mais próximo | Divisão e conquista | O(n log n) |

## Git / entrega
O enunciado pede repositório Git com histórico de commits ao longo do desenvolvimento. Depois de revisar os arquivos:
```bash
git init
git add .
git commit -m "Implementa algoritmos e testes iniciais"
git add .
git commit -m "Adiciona benchmarks e relatório experimental"
```
Crie um repositório vazio no GitHub e conecte:
```bash
git branch -M main
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```
Não invente um histórico retroativo: faça commits reais à medida que revisar e completar o trabalho.
