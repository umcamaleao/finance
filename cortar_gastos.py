from itertools import accumulate

def patrimonio_anual(anos, inicial, corte_por_ano, juros):
    renda_anual = [inicial] + [corte_por_ano for _ in range(anos)]
    return list(accumulate(renda_anual, lambda total, anual: total*juros + anual))

def cozinhar(anos, inicial=1000, corte_por_ano=1820):
    return patrimonio_anual(anos=anos, inicial=inicial, corte_por_ano=corte_por_ano, juros=1.04)

def investir(anos, inicial=1000, juros=1.06):
    return patrimonio_anual(anos=anos, inicial=inicial, corte_por_ano=0, juros=juros)

def comparar(inicial, juros=1.06, corte_por_ano=1820):
    return(inicial,
           cozinhar(anos=10, inicial=inicial, corte_por_ano=corte_por_ano)[-1],
           investir(anod=10, inicial=inicial, juros=juros)[-1])


if __name__ == '__main__':
	print(comparar(1000))
