gsql -g invest_graph 'DROP QUERY ALL'
gsql -g invest_graph 'DROP JOB ALL'
gsql 'DROP GRAPH invest_graph'

gsql schema_invest_graph.gsql
gsql loading/load_invest_graph.gsql

gsql -g payment_fraud queries/Absolute_Holding_Model.gsql
gsql -g payment_fraud queries/Through_Holding_Model.gsql
gsql -g payment_fraud queries/Single_Major_Shareholder_Model.gsql
gsql -g payment_fraud queries/run_models.gsql
gsql -g payment_fraud queries/find_import_company.gsql
gsql -g payment_fraud 'INSTALL QUERY ALL'