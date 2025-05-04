import json
import sys

if len(sys.argv) != 4:
    print("Нужно указать 3 файла: values.json, tests.json, report.json")
    exit()

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file) as f:
    values = json.load(f)

with open(tests_file) as f:
    tests = json.load(f)


def insert_values(test_list, values_list):
    for test in test_list:
        if "id" in tests:
            for v in values_list:
                if v["id"] == test["id"]:
                    test["value"] = v["value"]
                    break
        if "values" in test:
            insert_values(test["values"], values_list)


insert_values(tests["tests"], values)

with open(report_file, 'w') as f:
    json.dump(tests, f, indent=2)
