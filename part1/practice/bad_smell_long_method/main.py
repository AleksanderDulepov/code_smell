# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list(input_str:str):
    data=_read(input_str)
    data=_sort(data)
    data=_filter(data)
    return data

def _read(input_str):
    result_list=input_str.split('\n')
    result_list=[i.split(';') for i in result_list]
    return result_list

def _sort(input_list:list):
    return sorted(input_list, key=lambda x: int(x[1]))

def _filter(input_list:list):
    return [i for i in input_list if int(i[1])>10]

if __name__ == '__main__':
    print(get_users_list(csv))
