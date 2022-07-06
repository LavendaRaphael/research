# Cluster

## Torque

interactive

```sh
qsub -I -l nodes=<nodename> -q <queuename>
```

specific node

<http://docs.adaptivecomputing.com/torque/4-0-2/Content/topics/2-jobs/requestingRes.htm>

```sh
qsub -l nodes=b2005+b1803+b1813
```

misc

```sh
qstat -ls
bjobs
pestat
qselect -u <username> | xargs qdel
```
