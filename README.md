# sift grpc enabled
AI4EU (acumos) component to compute sift features of one image

This component is a modification of the flexible opencv component (see https://github.com/DuarteMRAlves/opencv-grpc-service).
See https://github.com/andrejfsantos4/DIY-gRPCcomponent for a tutorial on how to create your own components and to help interpret the code

This component can be downloaded from docker hub : docker pull  jpcosteira/aispsift

buildme - bash command to create the docker container
runme - launch the service. The tcp port is the same used in the testing script (see tests folder)

input: Image
output: Image and sift keypoints (coordinates and descriptor).

See test notebook for details (test_image_generic.ipynb in tests folder)

```shell
$ docker run --rm -it -p 8061:8061 -v pathtoexternal/externalfile.py=/workspace/external.py jpcosteira/aispsift:<specific tag>-latest
```
