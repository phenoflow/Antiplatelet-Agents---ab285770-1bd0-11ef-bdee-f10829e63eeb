# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"59021","system":"gprdproduct"},{"code":"34","system":"gprdproduct"},{"code":"60777","system":"gprdproduct"},{"code":"58331","system":"gprdproduct"},{"code":"51561","system":"gprdproduct"},{"code":"59253","system":"gprdproduct"},{"code":"53178","system":"gprdproduct"},{"code":"66563","system":"gprdproduct"},{"code":"53804","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('antiplatelet-agents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["antiplatelet-agents-gastroresistant---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["antiplatelet-agents-gastroresistant---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["antiplatelet-agents-gastroresistant---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
