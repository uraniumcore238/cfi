import csv
import allure

from pathlib import Path
from app import tests


@allure.step('Read data from csv file')
def data_generator(file_name):
    path_to_file = Path(tests.__file__).parent.parent.joinpath(f'test_parameters/{file_name}')
    list_of_parameters = []
    with open(path_to_file, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file, delimiter=',', quotechar='”', quoting=csv.QUOTE_ALL, escapechar='\\')
        next(csvreader)
        for row in csvreader:
            list_of_parameters.append(tuple(row))
    return list_of_parameters
