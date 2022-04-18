import datetime
import json
import time
import sys
import pandas as pd
def data_transfer(inputfile,outputfile):
    with open (inputfile,"r") as f:
        with open (outputfile,"w") as f1:
            lines = f.readlines()
            for i in lines:
                js2 = json.loads(i)
                if "company_number" in js2.keys():
                    company = js2['company_number']
                    address_line_1 = ""
                    address_line_2 = ""
                    country = ""
                    locality = ""
                    postal_code = ""
                    premises = ""
                    region = ""
                    if "address" in js2["data"].keys():
                        if "address_line_1" in js2['data']['address'].keys():
                            address_line_1 = js2['data']['address']['address_line_1']
                        if "address_line_2" in js2['data']['address'].keys():
                            address_line_2 = js2['data']['address']['address_line_2']
                        if "country" in js2['data']['address'].keys():
                            country = js2['data']['address']['country']
                        if "locality" in js2['data']['address'].keys():
                            locality = js2['data']['address']['locality']
                        if "postal_code" in js2['data']['address'].keys():
                            postal_code = js2['data']['address']['postal_code']
                        if "premises" in js2['data']['address'].keys():
                            premises = js2['data']['address']['premises']
                        if "region" in js2['data']['address'].keys():
                            region = js2['data']['address']['region']
                    ceased_on = ""
                    country_of_residence = ""
                    etag = ""
                    kind = ""
                    links = ""
                    name = ""
                    nationality = ""
                    natures_of_control = ""
                    notified_on = ""
                    is_control = 0
                    if "ceased_on" in js2['data'].keys():
                        ceased_on = js2['data']['ceased_on']
                    if "country_of_residence" in js2['data'].keys():
                        country_of_residence = js2['data']['country_of_residence']
                    if "etag" in js2['data'].keys():
                        etag = js2['data']['etag']
                    if "kind" in js2['data'].keys():
                        kind = js2['data']['kind']
                    if "links" in js2['data'].keys():
                        links = js2['data']['links']['self']
                    if "name" in js2['data'].keys():
                        name = js2['data']['name']
                    if "nationality" in js2['data'].keys():
                        nationality = js2['data']['nationality']
                    if "natures_of_control" in js2['data'].keys():
                        natures_of_control = js2['data']['natures_of_control']
                        if "ownership-of-shares-50-to-75-percent" in natures_of_control:
                            is_control = 1
                        if "ownership-of-shares-75-to-100-percent" in natures_of_control:
                            is_control = 1
                    if "notified_on" in js2['data'].keys():
                        notified_on = js2['data']['notified_on']
                    month = ""
                    year = ""
                    cday = ""
                    if "date_of_birth" in js2['data'].keys():
                        if "month" in js2['data']['date_of_birth'].keys():
                            month = js2['data']['date_of_birth']['month']
                        if "year" in js2['data']['date_of_birth'].keys():
                            year = js2['data']['date_of_birth']['year']
                        date = str(year) + "-" + str(month)
                        cday = str(datetime.datetime.strptime(date, '%Y-%m'))
                    all_str = company + "|"+ address_line_1 + "|" + address_line_2 + "|" + country + "|" + locality + "|" + postal_code + "|" + premises + "|" + region + "|" + ceased_on + "|" + country_of_residence + "|" + etag + "|" +  kind + "|" + links + "|" + name + "|" + nationality  + "|" + notified_on + "|" + cday + "|" + str(is_control) +"\n"
                    f1.write(all_str)
    
def spilt_str(str1,index):
    list1 = str1.split("/")
    return list1[index]
def data_format(inputfile,pcs_file,invest_file):
    t1 = pd.read_csv(inputfile,names=["company","address_line_1","address_line_2","country","locality","postal_code","premises","region","ceased_on","country_of_residence","etag","kind","links","name","nationality","notified_on","cday","is_control"],dtype={"company":str,"address_line_1":str,"address_line_2":str,"country":str,"locality":str,"postal_code":str,"premises":str,"region":str,"ceased_on":str,"country_of_residence":str,"etag":str,"kind":str,"links":str,"name":str,"nationality":str,"notified_on":str,"cday":str,"is_control":str},sep="|")
    t1['person_id'] = t1['links'].apply(spilt_str,index=-1)
    tmp = t1[(t1['kind'] == "corporate-entity-person-with-significant-control") &(t1['name'] != "")]
    tmp.to_csv(invest_file,index=False,sep="|")
    t2 = t1[t1['kind'] != "corporate-entity-person-with-significant-control"]
    t2.to_csv(pcs_file,index=False,sep="|")
                
if __name__ == "__main__":
    t0 = time.time()
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    pcs_file = sys.argv[3]
    invest_file = sys.argv[4]
    #print(inputfile,outputfile)
    data_transfer(inputfile,outputfile)
    t1 = time.time()
    print("data_transfer used:{:.2f}s".format(t1-t0))
    data_format(outputfile,pcs_file,invest_file)
    t2 = time.time()
    print("data_format used:{:.2f}s".format(t2-t1))