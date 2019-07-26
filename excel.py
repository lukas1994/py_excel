import formulas

file_name = "assets.xlsx"
def ref(cell, sheet="Capex Schedule"):
	return f"'[{file_name.upper()}]{sheet.upper()}'!{cell.upper()}"

xls = formulas.ExcelModel().loads(file_name).finish()
print(xls.calculate())
# xls = formulas.ExcelModel().loads("fund.xlsx").finish(circular=True)
f = xls.compile(inputs=[ref("D6"), ref("F7"), ref("E9")], outputs=[ref("v17")])
print(f(0,0,0))
g = lambda x: f(x).value[0,0]
print(g(1), g(10))

