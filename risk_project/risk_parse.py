#!/usr/bin/env python
# -*- coding: utf-8 -*-

code_with_risks_lst = []

with open('risks_base_info_portal.txt', 'r') as base_file:
    new_line = base_file.readline()
    while new_line:
        lst_from_txt = new_line.split('\t')

        risks_list = lst_from_txt[-1][:-1].split(';')

        for el in risks_list:
            lst = lst_from_txt[:2]
            lst.append(el)
            code_with_risks_lst.append(lst)


        new_line = base_file.readline()

print(code_with_risks_lst)

risks_info_lst = {}
with open('risks_portal.txt', 'r') as risks_file:
    risk_info = risks_file.readline()
    while risk_info:
        risk = risk_info.split('\t')
        risks_info_lst[risk.pop(0)] = risk
        risk_info = risks_file.readline()

print(risks_info_lst)
ready_lst = []
for prg_risk in code_with_risks_lst:
    for key in risks_info_lst.keys():
        if prg_risk[-1] == key:
            new_txt = prg_risk + risks_info_lst[key]
            ready_lst.append(new_txt)

print(ready_lst)
with open('formatted_file.txt', 'w') as final_file:
    for el in ready_lst:
        final_file.write("\t".join(el))




