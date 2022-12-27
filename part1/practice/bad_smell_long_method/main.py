# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list():
    data = _read()
    data_sorted = _sort(data)
    data_filtered = _filter(data_sorted)
    return data_filtered

def _read():
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data

def _sort(data):
    return sorted(data, key=lambda d: d['age'])

def _filter(data):
    data_filtered = []
    for item in data:
        if item['age'] > 10:
            data_filtered.append(item)
        else:
            continue
    return data_filtered




if __name__ == '__main__':
    print(get_users_list())
