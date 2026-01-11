## Install Postgress: 

In case we need a 
OpenShift Cluster (OCP-V) - IBM Cloud

### First, allow container to run as root:

`oc adm policy add-scc-to-user anyuid -z default -n <namespace/project>`

e.g `oc adm policy add-scc-to-user anyuid -z default -n project-expensedb`

### Then run following command for each files in given sequence. 

```oc apply -f <filename.yaml>```

1.  pvc.yaml
2.  secret.yaml
3.  deployment.yaml
4.  service.yaml

### Review postgres db 

```oc describe pod -n default -l app=<postgres-expensedb>```

```oc logs -n default -l app=<postgres-expensedb>```

### Forward port for local use 

```oc port-forward deployment/<postgres-expensedb> 5432:5432```

### Test postgres and find tables

```psql -h localhost -U <your_username> -d <your_database>```

```psql -h localhost -U expensedb_user -d expensedb_db```

```\d```

```\q```