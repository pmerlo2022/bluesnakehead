#!/usr/bin/python3
import codecs
import csv
import getopt
import json
import os
import ruamel.yaml
import shutil
import sys
import traceback
#import yaml

input_file = 'NULL'
output_dir = '/tmp'
monitoring_dir = "/opt/abj/source_of_truth/hosts"

##
#
#  This will take a CSV formatted file and create a single 
#  JSON inventory file.  
#
##
def csv_to_json(csvfile,directory):
    #read csv file
    data = {}
    outputfile = directory+"/dc_name_inventory.json"
    with open(csvfile, encoding='utf-8') as csvf:
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        #convert each csv row into python dict
        for row in csvReader:
          key = row['dc_name']
          data[key] = row

    csvf.close()
    #convert python jsonArray to JSON String and write to file
    with open(outputfile, 'w', encoding='utf-8') as jsonf:
      jsonf.write(json.dumps(data, indent=4))
    jsonf.close()


##
#
#  This will take a CSV formatted file and create a YAML from 
#  each line
#
##

def csv_to_yaml(csvFileInput, directory ):
    with open(csvFileInput, 'rb') as csvFile:
        csvOpen = csv.reader(codecs.iterdecode(csvFile, 'utf-8'))
        keys = next(csvOpen)
        for row in csvOpen:
            data = dict(zip(keys,row))
            systemname = data['dc_name']
            if (len(systemname) > 1):

              outputYAML = directory+"/"+data['dc_name']+".yml"
              outputJSON = directory+"/"+data['dc_name']+".json"
              yaml = ruamel.yaml.YAML()

              yamlfile = open(outputYAML, 'w')
              jsonfile = open(outputJSON, 'w')

              yaml.dump(data, yamlfile)
              json.dump(data, jsonfile)

              yamlfile.close()
              jsonfile.close()
              shutil.copy(outputJSON,monitoring_dir)

    csvFile.close()

def usage():
  print('USAGE -i input_file -o output_dir')
  exit()

##
#
#   MAIN 
#
##
argv = sys.argv[1:]
if (len(argv) == 0): usage()

try:
  directory=''
  input_file=''
  options,remainder = getopt.getopt(argv,'i:o:',['input=','output='])
  for opt, arg in options:
    if opt in ('-o', '--output'):
      directory = arg
    elif opt in ('-i', '--input'):
      input_file = arg

  #
  # remove tabs and blank lines
  #
  remove_tab=directory+'/.remove_tabs'
  if os.path.exists(remove_tab):
    os.remove(remove_tab)
  with open(input_file,'r') as fin, open(remove_tab,'w') as fout:
    for line in fin:
      # if the line is pretty much blank then skip over it.
      if len(line) < 2:
        continue
      else:
        # rplace the tabs with a ","
        newline = line.replace('\t',',')
#        fout.write(newline.lower())
        fout.write(newline)
    fin.close()
    fout.close()

  #
  #  this will take the big CSV and 
  #  write it to multiple YML files.
  #
  csv_to_yaml( remove_tab, directory )
  csv_to_json( remove_tab, directory )

  shutil.move(remove_tab,input_file)

except Exception as e:
  traceback.print_exc()
  print(e)
  usage()
