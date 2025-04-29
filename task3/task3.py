import json

values_file = 'values.json'
tests_file = 'tests.json'
report_file = 'report.json'


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def fill_values(tests, values):
    for key, value in tests.items():
        if isinstance(value, dict):
            fill_values(value, values)
        elif key == "id" and isinstance(value, str):
            test_id = int(value)
            for val in values:
                if val['id'] == test_id:
                    tests[key] = val['value']
                    break


values = read_json(values_file)
tests = read_json(tests_file)

fill_values(tests, values)

write_json(tests, report_file)
