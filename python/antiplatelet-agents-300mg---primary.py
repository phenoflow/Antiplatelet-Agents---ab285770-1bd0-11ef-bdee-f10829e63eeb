# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"49220","system":"gprdproduct"},{"code":"52905","system":"gprdproduct"},{"code":"56007","system":"gprdproduct"},{"code":"60278","system":"gprdproduct"},{"code":"53622","system":"gprdproduct"},{"code":"53816","system":"gprdproduct"},{"code":"53711","system":"gprdproduct"},{"code":"56736","system":"gprdproduct"},{"code":"54526","system":"gprdproduct"},{"code":"50555","system":"gprdproduct"},{"code":"52280","system":"gprdproduct"},{"code":"48165","system":"gprdproduct"},{"code":"54734","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('antiplatelet-agents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["antiplatelet-agents-300mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["antiplatelet-agents-300mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["antiplatelet-agents-300mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
