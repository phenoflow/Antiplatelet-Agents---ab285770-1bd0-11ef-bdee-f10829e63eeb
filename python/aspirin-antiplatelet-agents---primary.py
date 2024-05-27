# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"48974","system":"gprdproduct"},{"code":"16","system":"gprdproduct"},{"code":"59728","system":"gprdproduct"},{"code":"60127","system":"gprdproduct"},{"code":"56883","system":"gprdproduct"},{"code":"50949","system":"gprdproduct"},{"code":"54430","system":"gprdproduct"},{"code":"66861","system":"gprdproduct"},{"code":"64071","system":"gprdproduct"},{"code":"31938","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('antiplatelet-agents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["aspirin-antiplatelet-agents---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["aspirin-antiplatelet-agents---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["aspirin-antiplatelet-agents---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
