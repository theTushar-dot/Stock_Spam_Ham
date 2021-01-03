import csv as cs
import numpy as np
import random


def load_file(filename):
    with open(filename, 'r') as new_file:
        line = cs.reader(new_file)
        data = list(line)
        data.remove(data[0])
    return data


def dict_creator(data_set):
    main_dic = {1: [],
                0: []}

    for i in range(len(data_set)):
        if data_set[i][1] == '1':
            main_dic[1].append(data_set[i][0])
        else:
            main_dic[0].append(data_set[i][0])

    return main_dic


def classifier(dict_sample):
    n_true = len(dict_sample[1])
    n_false = len(dict_sample[0])
    main_dic_1 = {1: {},
                  0: {}}
    list_check = ['is', 'am', 'a', 'in', 'the', 'at', 'for', 'our', 'get', 'your', 'and', 'with', 'of', 'on', 'has']

    for i in range(n_true):
        new_list = dict_sample[1][i].split()
        list_2 = []

        for j in range(len(new_list)):
            if new_list[j] not in list_2:
                list_2.append(new_list[j])
            else:
                pass

        for k in range(len(list_2)):
            if list_2[k] not in list_check:
                if list_2[k] not in main_dic_1[1]:
                    main_dic_1[1][list_2[k]] = 1
                else:
                    main_dic_1[1][list_2[k]] += 1
            else:
                pass

    i = j = k = 0
    for i in range(n_false):
        new_list_1 = dict_sample[0][i].split()
        list_3 = []

        for j in range(len(new_list_1)):
            if new_list_1[j] not in list_3:
                list_3.append(new_list_1[j])
            else:
                pass

        for k in range(len(list_3)):
            if list_3[k] not in list_check:
                if list_3[k] not in main_dic_1[0]:
                    main_dic_1[0][list_3[k]] = 1
                else:
                    main_dic_1[0][list_3[k]] += 1
            else:
                pass

    return main_dic_1


def predict(testing_str, input_dict, t_num, f_num, all_num):
    p_y = t_num/all_num
    p_not_y = f_num/all_num
    list_n_1 = testing_str.split()
    list_after_clean = []
    p_x = 1
    p_not_x = 1

    for j in range(len(list_n_1)):
        if list_n_1[j] not in list_after_clean:
            list_after_clean.append(list_n_1[j])
        else:
            pass

    for i in range(len(list_after_clean)):
        if list_after_clean[i] in input_dict[1].keys():
            p_x *= input_dict[1][list_after_clean[i]]/t_num
        else:
            pass

        if list_after_clean[i] in input_dict[0].keys():
            p_not_x *= input_dict[0][list_after_clean[i]]/f_num
        else:
            pass

    if p_x == 1:
        p_x = 0
    else:
        pass
    if p_not_x == 1:
        p_not_x = 0
    else:
        pass

    final_pro = ((p_x*p_y)/(p_x*p_y + p_not_x*p_not_y))
    return final_pro

def main():
    data1 = load_file('market_spam.csv')

    dic_1 = dict_creator(data1)

    num_true = len(dic_1[1])
    num_false = len(dic_1[0])
    n_number = len(dic_1[1]) + len(dic_1[0])

    final_dict = classifier(dic_1)
    print(final_dict)

    test_string = input("Enter:")

    result = predict(test_string, final_dict, num_true, num_false, n_number)

    print(result)

if __name__ == '__main__':
    main()

