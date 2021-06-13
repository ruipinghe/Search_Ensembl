from django.shortcuts import render
from .forms import HouseChoiceForm
from django.http import HttpResponseRedirect


from fake_useragent import UserAgent
import requests


import mysql.connector



# Create your views here.

def search_data(request):
    """定义页面的展示格式，表格+分页"""
    form = HouseChoiceForm()

    return render(request, 'homelink/index.html', {'form': form, })



def search_result(request):
    if request.method == 'POST':
        form = HouseChoiceForm(request.POST)
        if form.is_valid():
            species = form.cleaned_data.get('dbname')
            dbtype = form.cleaned_data.get('dbtype')
            release = form.cleaned_data.get('release')
        data_list = data_query(species, dbtype, release)
        return render(request, 'homelink/results.html', {'my_list': data_list})
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

    cursor = cnx.cursor()
    cursor.execute(sql)
    cresults = cursor.fetchall()
    data_list = []
    
    for i in cresults:
        data_list.append({'dbname':i[0],'type':i[1]})
    
    cnx.close()
    cursor.close()
    return data_list


    
