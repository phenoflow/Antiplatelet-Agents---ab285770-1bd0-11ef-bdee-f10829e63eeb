# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Iain Buchan, Naveed Sattar, Martin K Rutter, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"56996","system":"gprdproduct"},{"code":"66345","system":"gprdproduct"},{"code":"50926","system":"gprdproduct"},{"code":"56995","system":"gprdproduct"},{"code":"49685","system":"gprdproduct"},{"code":"31211","system":"gprdproduct"},{"code":"54284","system":"gprdproduct"},{"code":"34942","system":"gprdproduct"},{"code":"33320","system":"gprdproduct"},{"code":"33676","system":"gprdproduct"},{"code":"54565","system":"gprdproduct"},{"code":"31954","system":"gprdproduct"},{"code":"59791","system":"gprdproduct"},{"code":"66546","system":"gprdproduct"},{"code":"31953","system":"gprdproduct"},{"code":"34434","system":"gprdproduct"},{"code":"57057","system":"gprdproduct"},{"code":"52618","system":"gprdproduct"},{"code":"54997","system":"gprdproduct"},{"code":"3","system":"gprdproduct"},{"code":"49060","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('antiplatelet-agents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["dispersible-antiplatelet-agents---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["dispersible-antiplatelet-agents---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["dispersible-antiplatelet-agents---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
