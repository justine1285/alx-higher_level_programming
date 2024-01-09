#!/usr/bin/python3
"""Adds arguments to a python list"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []

arguments = sys.argv[1:]

if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

my_list.extend(arguments)

save_to_json_file(my_list, "add_item.json")
