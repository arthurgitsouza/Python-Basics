#Pedi para o chat gpt trazer os dados do brasileirão no ano de 2024 no dia em que fiz esse exercicio, dia 27 de Junho de 2024, Aliás, o mengão tá de liderrrrrr.
times_brasileirao_2024 = (
    'Flamengo',      # 1º
    'Botafogo',      # 2º
    'Palmeiras',     # 3º
    'Fortaleza',     # 4º
    'Cruzeiro',      # 5º
    'São Paulo',     # 6º
    'Bahia',         # 7º
    'Athletico-PR',  # 8º
    'Grêmio',        # 9º
    'Internacional', # 10º
    'Fluminense',    # 11º
    'Atlético-MG',   # 12º
    'Cuiabá',        # 13º
    'Corinthians',   # 14º
    'Santos',        # 15º
    'Vasco',         # 16º
    'América-MG',    # 17º
    'Coritiba',      # 18º
    'Goiás',         # 19º
    'Red Bull Bragantino' # 20º
)

print('-='*20)
print(f'Lista de times do Brasileirão: {times_brasileirao_2024}')
print('-='*20)
print(f'Os 5 primeiros são: {times_brasileirao_2024[0:5]}')
print('-='*20)
print(f'Os 4 últimos são: {times_brasileirao_2024}[-4]')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times_brasileirao_2024)}')
print('-='*20)
print(f'O Flamengo está na {times_brasileirao_2024.index("Flamengo")+1}ª posição!' ) 