import csv
from re import sub, findall


with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def merge_records(record_one, record_two):
    '''Функция убирающая дубли'''
    result = list()
    for index in range(len(record_one)):
        result.append(record_one[index]) if record_one[index] else result.append(record_two[index])
    return result


num_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
num_pattern_new = r'+7(\2)-\3-\4-\5 \6\7'


contacts = list()
for row in contacts_list:
    record = list()
    complete_name = findall(r'(\w+)', ' '.join(row[:3]))
    complete_name.append('') if len(complete_name) < 3 else ...
    record += complete_name
    record.append(row[3])
    record.append(row[4])
    record.append(sub(num_pattern, num_pattern_new, row[5]).strip())
    record.append(row[6])
    contacts.append(record)


contact_dict = dict()
for item in contacts:
    contact_dict[item[0]] = merge_records(item, contact_dict[item[0]]) if item[0] in contact_dict else item


if __name__ == '__main__':

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')

        ## Вместо contacts_list подставьте свой список:
        datawriter.writerows(contact_dict.values())