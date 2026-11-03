import argparse
import json
from algoritmos import (
    max_subarray_bruteforce, max_subarray_divide_conquer, max_subarray_kadane,
    closest_pair_bruteforce, closest_pair_divide_conquer
)

def main():
    parser = argparse.ArgumentParser(description="Trabalho prático: Divisão e Conquista")
    parser.add_argument("problema", choices=["soma", "pontos"])
    parser.add_argument("--metodo", choices=["forca-bruta", "divisao-conquista", "kadane"],
                        default="divisao-conquista")
    parser.add_argument("--entrada", required=True, help="Arquivo JSON com os dados")
    args = parser.parse_args()
    with open(args.entrada, encoding="utf-8") as f:
        dados = json.load(f)

    if args.problema == "soma":
        vetor = dados["vetor"]
        funcoes = {
            "forca-bruta": max_subarray_bruteforce,
            "divisao-conquista": max_subarray_divide_conquer,
            "kadane": max_subarray_kadane,
        }
        print("Soma máxima, início, fim:", funcoes[args.metodo](vetor))
    else:
        pontos = [tuple(p) for p in dados["pontos"]]
        funcoes = {
            "forca-bruta": closest_pair_bruteforce,
            "divisao-conquista": closest_pair_divide_conquer,
        }
        distancia, i, j = funcoes[args.metodo](pontos)
        print(f"Distância: {distancia:.6f}")
        print(f"Índices: {i}, {j}")
        print(f"Pontos: {pontos[i]} e {pontos[j]}")

if __name__ == "__main__":
    main()
