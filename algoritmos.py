"""Implementações do trabalho de Divisão e Conquista.

Índices retornados para subarranjo são baseados em zero e incluem início/fim.
Pontos são pares (x, y). Para pares empatados, a escolha é determinística.
"""
from math import hypot, inf


def _melhor(a, b):
    """Escolhe maior soma; em empate, menor início e depois menor fim."""
    if a[0] != b[0]:
        return a if a[0] > b[0] else b
    return a if (a[1], a[2]) <= (b[1], b[2]) else b


def max_subarray_bruteforce(v):
    if not v:
        raise ValueError("O vetor não pode ser vazio.")
    best = (v[0], 0, 0)
    for i in range(len(v)):
        total = 0
        for j in range(i, len(v)):
            total += v[j]
            best = _melhor(best, (total, i, j))
    return best


def max_subarray_divide_conquer(v):
    if not v:
        raise ValueError("O vetor não pode ser vazio.")

    def solve(lo, hi):
        if lo == hi:
            return (v[lo], lo, hi)
        mid = (lo + hi) // 2
        left = solve(lo, mid)
        right = solve(mid + 1, hi)

        total = 0
        best_left = (-inf, mid, mid)
        for i in range(mid, lo - 1, -1):
            total += v[i]
            best_left = _melhor(best_left, (total, i, mid))

        total = 0
        best_right = (-inf, mid + 1, mid + 1)
        for j in range(mid + 1, hi + 1):
            total += v[j]
            best_right = _melhor(best_right, (total, mid + 1, j))

        crossing = (best_left[0] + best_right[0], best_left[1], best_right[2])
        return _melhor(_melhor(left, right), crossing)

    return solve(0, len(v) - 1)


def max_subarray_kadane(v):
    """Versão O(n), incluída como questão-desafio indicada na avaliação."""
    if not v:
        raise ValueError("O vetor não pode ser vazio.")
    current_sum = best_sum = v[0]
    current_start = best_start = best_end = 0
    for i in range(1, len(v)):
        # Em empate, manter a extensão anterior favorece início menor.
        if current_sum + v[i] < v[i]:
            current_sum = v[i]
            current_start = i
        else:
            current_sum += v[i]
        candidate = (current_sum, current_start, i)
        best = (best_sum, best_start, best_end)
        chosen = _melhor(best, candidate)
        best_sum, best_start, best_end = chosen
    return (best_sum, best_start, best_end)


def _dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def closest_pair_bruteforce(points):
    if len(points) < 2:
        raise ValueError("São necessários pelo menos dois pontos.")
    best = (inf, None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d2 = _dist2(points[i], points[j])
            candidate = (d2, i, j)
            if d2 < best[0] or (d2 == best[0] and (i, j) < (best[1], best[2])):
                best = candidate
    return (best[0] ** 0.5, best[1], best[2])


def closest_pair_divide_conquer(points):
    """O(n log n): pré-ordena por x/y e examina até 7 vizinhos na faixa."""
    n = len(points)
    if n < 2:
        raise ValueError("São necessários pelo menos dois pontos.")

    # Identificador original permite tratar pontos repetidos sem ambiguidade.
    px = sorted((p[0], p[1], i) for i, p in enumerate(points))
    py = sorted(((p[0], p[1], i) for i, p in enumerate(points)), key=lambda p: (p[1], p[0], p[2]))

    def solve(xs, ys):
        m = len(xs)
        if m <= 3:
            best = (inf, None, None)
            for a in range(m):
                for b in range(a + 1, m):
                    ia, ib = xs[a][2], xs[b][2]
                    d2 = _dist2(points[ia], points[ib])
                    pair = (min(ia, ib), max(ia, ib))
                    if d2 < best[0] or (d2 == best[0] and pair < (best[1], best[2])):
                        best = (d2, pair[0], pair[1])
            return best

        mid = m // 2
        left_x, right_x = xs[:mid], xs[mid:]
        left_ids = {p[2] for p in left_x}
        left_y = [p for p in ys if p[2] in left_ids]
        right_y = [p for p in ys if p[2] not in left_ids]

        dl = solve(left_x, left_y)
        dr = solve(right_x, right_y)
        best = dl if (dl[0], dl[1], dl[2]) <= (dr[0], dr[1], dr[2]) else dr
        delta2 = best[0]
        mid_x = right_x[0][0]
        strip = [p for p in ys if (p[0] - mid_x) ** 2 <= delta2]

        for i in range(len(strip)):
            # Propriedade geométrica: bastam no máximo 7 sucessores em y.
            for j in range(i + 1, min(i + 8, len(strip))):
                dy = strip[j][1] - strip[i][1]
                if dy * dy > best[0]:
                    break
                ia, ib = strip[i][2], strip[j][2]
                pair = (min(ia, ib), max(ia, ib))
                d2 = _dist2(points[ia], points[ib])
                if d2 < best[0] or (d2 == best[0] and pair < (best[1], best[2])):
                    best = (d2, pair[0], pair[1])
        return best

    d2, i, j = solve(px, py)
    return (d2 ** 0.5, i, j)
