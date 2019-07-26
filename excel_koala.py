from koala.ExcelCompiler import ExcelCompiler

file_name = "assets.xlsx"
def ref(cell, sheet="Capex Schedule"):
	return f"{sheet}!{cell}"

sp = ExcelCompiler(file_name).spreadsheet
print(sp.asdict())
print(dir(sp))
inputs = [ref("D6"), ref("F7"), ref("E9")]
output = ref("V17")
sp.gen_graph(inputs=inputs, outputs=[output])
# sp.prune_graph()
sp.cell_reset(output)

def f(tax_rate, inflation_rate, value_rate):
	sp.cell_set_value(inputs[0], tax_rate)
	sp.cell_set_value(inputs[1], inflation_rate)
	sp.cell_set_value(inputs[2], value_rate)
	return sp.cell_evaluate(output)

print(f(0.3, 0.03, 1))

print(sp.cell_evaluate(ref("D17")))
print(sp.cell_evaluate(ref("E17")))
print(sp.cell_evaluate(ref("F17")))
print(sp.cell_evaluate(ref("G17")))
