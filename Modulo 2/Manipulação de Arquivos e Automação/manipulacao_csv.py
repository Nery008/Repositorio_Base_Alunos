import csv

with open('lista_de_compras.tsv', 'w', newline='', encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n')

    csvWriter.writerow(['maçã, banana, uva'])
    csvWriter.writerow(['maçã, banana, uva'])
    csvWriter.writerow(['maçã, banana, uva'])
