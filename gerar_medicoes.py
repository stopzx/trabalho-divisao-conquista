import csv, random, statistics, time, platform, sys
from pathlib import Path
from algoritmos import (max_subarray_bruteforce, max_subarray_divide_conquer,
                        max_subarray_kadane, closest_pair_bruteforce,
                        closest_pair_divide_conquer)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dados"
OUT.mkdir(exist_ok=True)
SIZES = [100, 200, 400, 800, 1600, 3200, 6400]
REPEATS = 5
rng = random.Random(20261102)

def medir(func, data, repeats=REPEATS):
    tempos = []
    for _ in range(repeats):
        inicio = time.perf_counter()
        func(data)
        tempos.append(time.perf_counter() - inicio)
    return statistics.mean(tempos), tempos

def main():
    rows = []
    for n in SIZES:
        vetor = [rng.randint(-100, 100) for _ in range(n)]
        pontos = [(rng.randint(0, 10**6), rng.randint(0, 10**6)) for _ in range(n)]
        for nome, func, data in [
            ("soma_forca_bruta", max_subarray_bruteforce, vetor),
            ("soma_divisao_conquista", max_subarray_divide_conquer, vetor),
            ("soma_kadane", max_subarray_kadane, vetor),
            ("pontos_forca_bruta", closest_pair_bruteforce, pontos),
            ("pontos_divisao_conquista", closest_pair_divide_conquer, pontos),
        ]:
            media, tempos = medir(func, data)
            rows.append({
                "problema_algoritmo": nome, "n": n, "repeticoes": REPEATS,
                "tempos_segundos": ";".join(f"{t:.9f}" for t in tempos),
                "media_segundos": f"{media:.9f}"
            })
            print(nome, n, f"{media:.6f}s", flush=True)
    with (OUT / "medicoes.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    (OUT / "configuracao.txt").write_text(
        f"Sistema: {platform.platform()}\\nPython: {sys.version}\\n"
        f"Processador: {platform.processor() or 'não informado pelo sistema'}\\n"
        f"Repetições por tamanho: {REPEATS}\\nSemente aleatória: 20261102\\n",
        encoding="utf-8"
    )
    try:
        import matplotlib.pyplot as plt
        groups = {}
        for r in rows:
            groups.setdefault(r["problema_algoritmo"], ([], []))
            groups[r["problema_algoritmo"]][0].append(int(r["n"]))
            groups[r["problema_algoritmo"]][1].append(float(r["media_segundos"]))
        for prefix, names in {
            "subarranjo": ["soma_forca_bruta","soma_divisao_conquista","soma_kadane"],
            "pontos": ["pontos_forca_bruta","pontos_divisao_conquista"]
        }.items():
            plt.figure()
            for name in names:
                xs, ys = groups[name]
                plt.plot(xs, ys, marker="o", label=name.replace("_", " "))
            plt.xlabel("Tamanho da entrada (n)")
            plt.ylabel("Tempo médio (segundos)")
            plt.title("Desempenho — " + prefix)
            plt.grid(True); plt.legend(); plt.tight_layout()
            plt.savefig(OUT / f"grafico_{prefix}.png", dpi=160)
            plt.close()
    except ImportError:
        print("matplotlib não instalado; CSV gerado, gráficos não foram criados.")

if __name__ == "__main__":
    main()
