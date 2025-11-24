import camelot

tables = camelot.read_pdf("38.pdf", pages="1")

print("Total tables extracted:", tables.n)

# Print first table
print(tables[0].df)

tables.export("output.csv", f="csv")
