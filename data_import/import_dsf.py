import csv

from user.models import SalesPerson
from location.models import Branch

with open('dsf.csv') as csv_file:
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
        cleaned_name = ''
        for part_name in name_updated:
            cleaned_name += part_name + ' '
        dsf = SalesPerson()
        dsf.name = cleaned_name.strip()
        dsf.reporting_manager = None if line[1].strip(
        ) == '' else SalesPerson.persons.get(name=line[1].strip())
        dsf.branch_name = None if line[1].strip(
        ) == '' else dsf.reporting_manager.branch_name
        dsf.designation = None
        dsf.is_manager = False
        dsf.save()

        print("Added")
print("completed")
