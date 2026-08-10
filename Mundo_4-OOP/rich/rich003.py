from rich import print
from rich.table import Table

table = Table(title="Tabela de Preços")

table.add_column("Nome", justify='right', style='red')
table.add_column("Preço")
table.add_row("Lápis", "R$1,50")
table.add_row("Borracha", "R$5,00")

print(table)