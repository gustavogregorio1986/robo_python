from openpyxl import load_workbook
from openpyxl.utils import FORMULAE

wb = load_workbook("Fórmulas.xlsx")

sheet = wb["Vendas"]

# criando cabeçalho da coluna E
sheet["E1"] = "Valor Total"

for linha in range(3, 12):
    sheet[f"E{linha}"] = f"=C{linha}*D{linha}"

# verificando todos as fóermulas disponíveis
for i in FORMULAE:
    print(i)

# utilizando uma formula pronta
sheet["E12"] = "=SUM(E2:E11)"

sheet["D12"] = "=SUM(D2:D11)"

sheet["C12"] = "=SUM(C2:C11)"

wb.save("Fórmulas.xlsx")