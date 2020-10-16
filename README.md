# UC3-Portal

Download and Metadata Portal for the UNISDR-Data at https://gar.mnm-team.org

## Use Docker to build and run the portal

```
$ sudo docker build -t gar-portal . 
$ sudo docker run -it -p 9000:8080 --name gar -e DIR='/tmp' --rm gar-portal

```
## Environment Variables

```
-e DIR='PATH_TO_DIRECTORY'

```

Use this variable with docker run to specify which directory in the container
should be hosted. Be aware that due to the initial caching of file structure
and sizes, the first startup may take a while for large directories.
