# Cluster

## qsub

interactive

```sh
qsub -I -l nodes=<nodename> -q <queuename>
```

specific node

<http://docs.adaptivecomputing.com/torque/4-0-2/Content/topics/2-jobs/requestingRes.htm>

```sh
qsub -l nodes=b2005+b1803+b1813
```