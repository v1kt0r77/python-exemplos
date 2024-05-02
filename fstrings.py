#formatação de strings
from datetime import datetime
ano_atual = datetime.now().year
clube = 'spfc'
ano_fundação = 1930
campeonato_mundial = 3
print(f"{clube} possui {campeonato_mundial} titulos mundias.")
print(f"são {ano_atual - ano_fundação} anos de existência.")     