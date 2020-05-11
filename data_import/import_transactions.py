import csv
from datetime import datetime

from django.utils.dateparse import parse_datetime
from business.models import Transaction
from user.models import SalesPerson


with open('transactions2.csv') as csv_file:
    # Date Submission,Date Issued,Agent,Manager,Location,Contribution,Type,Status
    # submission_date = [0]
    # issuance_date = [1]
    # sales_person = [2] foreign key
    # amount = [5]
    # transaction_type[6]
    # transaction_status[7]
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)
        sales_person_cleaned_name = ''
        temp_name = line[2].split()
        for part_name in temp_name:
            part_name = part_name.lower()
            part_name = part_name.strip()
            part_name = part_name.capitalize()
            sales_person_cleaned_name += part_name + ' '
        sales_person_cleaned_name = sales_person_cleaned_name.strip()
        print(sales_person_cleaned_name)

        transaction = Transaction()
        transaction.submission_date = None if line[0].strip(
        ) == '' else datetime.strptime(line[0], '%Y-%m-%d')
        transaction.issuance_date = None if line[1].strip(
        ) == '' else datetime.strptime(line[1], '%Y-%m-%d')
        transaction.sales_person = None if line[2].strip(
            ' ') == '' else SalesPerson.persons.get(name=sales_person_cleaned_name)
        transaction.amount = None if line[5].strip() == '' else line[5]
        transaction.transaction_type = None if line[7].strip(
        ) == '' else line[7]
        transaction.transaction_status = None if line[8].strip(
        ) == '' else line[8]

        transaction.save()
