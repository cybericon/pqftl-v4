import csv

from user.models import SalesPerson
from location.models import Branch

with open('managers.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)
        name = line[0].split()
        name_updated = []
        for part_name in name:
            part_name = part_name.lower()
            part_name = part_name.strip()
            name_updated.append(part_name.capitalize())

        name_updated = f'{name_updated[0]} {name_updated[1]}'
        manager = SalesPerson()
        manager.name = name_updated
        manager.branch_name = None if line[1].strip(
        ) == '' else Branch.locations.get(name=line[1].strip())
        manager.designation = None
        manager.is_manager = True
        manager.reporting_manager = None
        manager.save()

        print(name_updated + " Added")
print("completed")
