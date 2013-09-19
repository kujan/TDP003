#!usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def load(filename):
    json_file = open(filename)
    db = json.load(json_file)
    json_file.close()
    print(db)
    return db


def get_project_count(db):
    return len(db)

def get_project(db, id):
    for project in db:
        if project["project_no"] == id:
            return project

    return None

def get_techniques(db):
    lista = []
    for techniques in db:
        if techniques["techniques_used"]:
            lista.extend(techniques["techniques_used"])
    return sorted(set(lista))

def get_techniques_stats(db):
    return get_techniques(db)

        

            

        
