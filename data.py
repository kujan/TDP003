#!usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def load(filename):
    """Laddar in en JSON fil och returnerar den som en lista"""
    try:
        json_file = open(filename)
    except:
        return None
    db = json.load(json_file)
    json_file.close()
    return db


def get_project_count(db):
    """Läser in hur många projekt vi har sparade"""
    return len(db)

def get_project(db, id):
    """Hämtar ett projekt genom att skriva vart det ska hämtas och id"""
    for project in db:
        if project["project_no"] == id:
            return project

    return None

def search(db, sort_by=u'start_date', sort_order=u'desc', techniques=None, search=None, search_fields=None):
    """Hämtar projekt som matchar det man har sökt på"""
    techniques_list  = []
    if techniques == None or techniques == []:
        techniques_list = db
    else:
        for projects in db:
            isTechInList = True
            for technique in techniques:
                if technique not in projects["techniques_used"]:
                    isTechInList = False
            if isTechInList:
                techniques_list.append(projects)
    #print(techniques_list)

    if search != None:
        search = search.lower()

    search_list = []
    if search_fields == None:
        search_list = techniques_list
    elif search_fields == []:
        return search_fields
    else:
        for searchIn in techniques_list:
            
            for field in search_fields:
                isSearchInList = True
                searchInText = str(searchIn[field])
                searchInText = searchInText.lower()
                
                if searchIn[field] == None:
                    searchInText = ""
            
                if searchInText.find(search) == -1:
                    isSearchInList = False
            
            if isSearchInList:
                search_list.append(searchIn)
                
    
    search_list = sort_list(search_list, sort_order, sort_by)
    return search_list


#def get_techniques(db):
   # techniques_list = []
   # for project in db:
       # for technique in project["techniques_used"]:
         #   if technique not in techniques_list:
            #    techniques_list.append(technique)
 #   techniques_list.sort()
  #  return techniques_list

def get_techniques(db):
    """Hämtar alla tekniker som finns i filen och sorterar dom i bokstavsordning"""
    lista = []
    for techniques in db:
        if techniques["techniques_used"]:
            lista.extend(techniques["techniques_used"])
    return sorted(set(lista))

def get_technique_stats(db):
    """Hämtar teknikerna och vilka projekt dom används i"""
    techniques_stats = {}
    techniques_list = get_techniques(db)
    for technique in techniques_list:
        projects_list = []
        for projects in db:
            if technique in projects["techniques_used"]:
                projects_list.append({"id" : projects["project_no"], "name" : projects["project_name"]})
        projects_list = sort_list(projects_list, order="asc", dictkey="name")

        techniques_stats[technique] = projects_list
    return techniques_stats
        

            
def sort_list(lista, order, dictkey):
    """Sorterar en lista i stigande eller sjunkande ordning och vad den ska sortera efter"""
    if order == "asc":
        lista = sorted(lista, key=lambda x: x[dictkey], reverse=False)    
    else:
        lista = sorted(lista, key=lambda x: x[dictkey], reverse=True)
    
    return lista
        

   
        
