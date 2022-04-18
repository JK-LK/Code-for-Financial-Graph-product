# Code-for-Financial-Graph-product

## Step 1 download psc dataset 
```
cd ./data
wget http://download.companieshouse.gov.uk/persons-with-significant-control-snapshot-2022-03-16.zip
tar -zxvf persons-with-significant-control-snapshot-2022-03-16.zip
```
## Step 2 Data processing 
```
nohup python data_processing.py ./data/persons-with-significant-control-snapshot-2022-03-16.txt ./data/data_0316.csv ./data/pcs_data.csv ./data/invest_edge.csv &
``` 

## Step 3 Add tigergraph UDF 
```
eval gsql 'PUT ExprFunctions FROM "./ExprFunctions.hpp"'
```

## Step 4 Build the project
```
bash build.sh
```