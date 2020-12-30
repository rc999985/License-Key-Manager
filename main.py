import csv

greeting = input("Would you like to start with a fresh dictionary?")
lic_dict = {}

def key_entry():
    while True:
        a = input("Please enter a license key name: ")
        b = input("Please enter a license key to store: ")
        lic_dict[a] = b
        c = input("Would you like to enter another? Press y for yes, or any other key for no.")
        if c == "y":
            continue
        else:
            w = csv.writer(open("output.csv", "w"))
            for key, val in lic_dict.items():
                w.writerow([key, val])
            print("Here are your keys: ")
            print(lic_dict)
            break

if greeting == 'y':
    key_entry()

else:
    with open('output.csv', mode='r') as infile:
        reader = csv.reader(infile)
        with open('output_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            lic_dict = {rows[0]:rows[1] for rows in reader}
    key_entry()