import csv
import sys
# person = [['1089311767400984576', '2019-01-26 23:58:58', 'JORGE FLOR'], ['1089311359614025729', '2019-01-26 23:57:21', 'VERONICA BARRENO'], ['1089310678454882314', '2019-01-26 23:54:38', 'JOSUE LEON R.'], ['1089310562079657984', '2019-01-26 23:54:11', 'MELISA LAMA'], ['1089310037644926976', '2019-01-26 23:52:06', 'JOSUE LEON R.'], ['1089308841488068613', '2019-01-26 23:47:20', 'EDDIE CASTILLO'], ['1089308548218216449', '2019-01-26 23:46:10', 'BRAYAN ABEL FRANCO PACHECO'], ['1089308300058021888', '2019-01-26 23:45:11', 'MANOLO CELLERI V.'], ['1089306425342521350', '2019-01-26 23:37:44', 'FIEBRE AMARILLA'], ['1089304210733236225', '2019-01-26 23:28:56', 'JORGE LUEY ORTEGA']]


# csv.register_dialect('myDialect',
# delimiter = ',',
# quoting=csv.QUOTE_NONE,s
# skipinitialspace=True)

# with open('dob2222.csv', 'w') as f:
#     writer = csv.writer(f, dialect='myDialect')
#     for row in person:
#     	writer.writerow(row)

# f.close()

class CSV_py():

	def generar_csv(self, nombreArchivo, titulos, dataSource):
		csv.register_dialect('myDialect',
			delimiter = ';',
			quoting = csv.QUOTE_NONE,
			skipinitialspace = False,
			escapechar=' ' 
			)
		with open(nombreArchivo+'.csv', 'w') as archivo:
			writer = csv.writer(archivo, dialect = 'myDialect')
			writer.writerow(titulos)
			for fila in dataSource:
				writer.writerow(fila)

		archivo.close()
