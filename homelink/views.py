from django.shortcuts import render
#from .models import HouseInfo
from .forms import HouseChoiceForm
#from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


from fake_useragent import UserAgent
import requests
#from bs4 import BeautifulSoup
#import re

import mysql.connector



# Create your views here.


#def house_index(request):
def search_data(request):
    """定义页面的展示格式，表格+分页"""
    form = HouseChoiceForm()
    '''
    if data_list:
        house_list = data_list
    else:
        house_list = HouseInfo.objects.all()
    #print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', HouseInfo.objects.all())
    
    house_list = [{'dbname':'human','dbtype':'core'}]
    print('house_listttttttttttttttttttttt', house_list)
    if house_list:
        paginator = Paginator(house_list, 50)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        print(paginator, page, page_obj)
        return render(request, 'homelink/index.html',
                      {'page_obj': page_obj, 'paginator': paginator,
                       'is_paginated': True, 'form': form, })
    else:
    '''

    return render(request, 'homelink/index.html', {'form': form, })



#def house_spider(request):
def search_result(request):
    if request.method == 'POST':
        form = HouseChoiceForm(request.POST)
        if form.is_valid():
            print('formisvalidddddddddddddddddd')
            species = form.cleaned_data.get('dbname')
            dbtype = form.cleaned_data.get('dbtype')
            release = form.cleaned_data.get('release')
            print(species, dbtype, release)
        data_list = data_query(species, dbtype, release)
        print('datalistlllllllllllllllllllllllllll:         ', data_list)

        #return house_index(request, data_list)
        return render(request, 'homelink/results.html', {'my_list': data_list})
        #return HttpResponseRedirect('/homelink/')
    else:
        return HttpResponseRedirect('/homelink/')   


def data_query(species, dbtype, release):
    
    if species == 'human':
        species = 'homo_sapiens'
    
    cnx = mysql.connector.connect(user='anonymous',host='ensembldb.ensembl.org',port='3306',database='ensembl_metadata_104')
    if dbtype == '':
        sql = "select dbname,type from genome_database where dbname LIKE" + " '"+ species + "%\_" + str(release) + "\_%'" + " ;" 
    else:
        sql = "select dbname,type from genome_database where dbname LIKE" + " '"+ species + "%\_" + str(release) + "\_%'" + " and type = " + "'"+str(dbtype)+"'" + " ;" 
    print(sql)

    cursor = cnx.cursor()
    cursor.execute(sql)
    cresults = cursor.fetchall()
    print('cresultsssssssssssssssssssssss', cresults )
    data_list = []
    
    for i in cresults:
        data_list.append({'dbname':i[0],'type':i[1]})
    
    cnx.close()
    cursor.close()
    return data_list


    
