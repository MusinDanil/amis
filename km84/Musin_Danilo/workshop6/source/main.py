"""
Тут написати умову до завдання
"""
import re


def get_dataset(path):
    try:
        with open(path) as inp:
            linenumber = 1
            inp.readline()
            for line in inp:
                line = line.strip().rstrip()
                if not line:
                    continue
                UID = get_element(line)
                PID = get_product_id(line)
                gender = get_gender(line)
                age = get_age(line)
                return UID, PID, gender, age

    except IOError as err:
        print('File ERROR', err.errno, '   ', err.strerror)
    except ValueError  as v_err:
        print('Value ERROR', v_err, '   ', linenumber)


def get_element(line):
    result = re.split(r',', line, maxsplit=1)
    element = result[0].strip()
    return element, result[1]


def get_product_id(line):
    element, tail = get_element(line)
    product_id = re.findall(r'\P\d{8}', element)[0]
    return product_id


def get_gender(line):
    element, tail = get_element(line)
    result = re.findall(r'[F|M]', element, 'i')[0]
    return result


def get_age(line):
    element, tail = get_element(line)
    result = re.findall(r'\d+\-\d+', element)[0]
    return result


if __name__ == "__main__":
    print(get_dataset('test.csv'))
