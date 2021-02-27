import qrcode
import csv


home = input("At home? If not press Enter ")
networkarray = []

if not home:
    with open("networkdata.csv") as file:
        for line in file:
             networkarray.append(line.strip().split(";"))

    if len(networkarray)>0:
        for i in range(0, len(networkarray)):
            print("[" + networkarray[i][0] + "] " + networkarray[i][1])

    network_selection= input("Choose Network from list or press Enter: ")
    if network_selection:
        for j in range(0, len(networkarray)):
            if network_selection == networkarray[j][0]:
                networkname = networkarray[j][2]
                password = networkarray[j][3]
                img = qrcode.make("WIFI:T:WPA;S:" + networkname + ";P:" + password + ";H:;")
                img.show()
                break;
    else:
        networkname = input("Networkname: ")
        password = input("Password: ")
        img = qrcode.make("WIFI:T:WPA;S:" + networkname + ";P:" + password + ";H:;")
        img.show()

        with open("networkdata.csv") as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=";")
            row_count = sum(1 for row in csv_reader)

        addToCsv = input("Add record to CSV? ")
        if addToCsv:
            network_owner = input("Who is the owner of the network? ")
            with open("networkdata.csv", "a", newline='') as csvfile:
                csvfilewr = csv.writer(csvfile, delimiter=";")
                csvfilewr.writerow([row_count + 1, network_owner, networkname, password])


else:
    img = qrcode.make("WIFI:T:WPA;*SSID here*;P:*Password here*;H:;")
    img.show()

