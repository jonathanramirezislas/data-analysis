"""
CSV reader options.
"""

import csv

def dictparse(csvfilename, keyfield, separator, quote, quotestrategy):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True,
                                   delimiter=separator,
                                    #ayuda a indicar que signo se va ausar como carater de citas
                                   quotechar=quote,
                                   #ver en las funciones de abajo su funcionalidad
                                   quoting=quotestrategy)
        for row in csvreader:
            table[row[keyfield]] = row
    return table, csvreader.fieldnames


def print_table(table, fieldnames):
    """
    Print out table, which must be a dictionary
    of dictionaries, in a nicely formatted way.
    """
    print("{:<19}".format(fieldnames[0]), end='')
    for field in fieldnames[1:]:
        print("{:>6}".format(field), end='')
    print("")
    for name, row in table.items():
        # Header column left justified
        print("{:<19}".format(name), end='')
        # Remaining columns right justified
        for field in fieldnames[1:]:
            print("{:>6}".format(row[field]), end='')
        print("", end='\n')

table, fieldnames = dictparse("hightemp.csv", 'City', ',', '"', csv.QUOTE_MINIMAL)
print(fieldnames)
print_table(table, fieldnames)

print("")
print("")

                                                            # Indica que cualquier cosa que no este entre quoute en ese caso "" va ser un numero y se represatara como tal por ello tenemos valores float ejemplo 65.0
table2, fieldnames2 = dictparse("hightemp2.csv", 'City', ',', '"', csv.QUOTE_NONNUMERIC)
print_table(table2, fieldnames2)

print("")
print("")

table3, fieldnames3 = dictparse("hightemp3.csv", 'City', ' ', '´', csv.QUOTE_NONNUMERIC)
print_table(table3, fieldnames3)