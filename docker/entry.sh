#!/bin/bash -x

CONTAINER_UID=$(test ! -z $HOST_UID && echo $HOST_UID || echo 9999)
CONTAINER_GID=$(test ! -z $HOST_GID && echo $HOST_GID || echo 9999)
PROXY_USERNAME=user

mkdir -m 1777 -p /tmp

echo "Starting with $CONTAINER_UID:$CONTAINER_GID"
groupadd -g $CONTAINER_GID -o $PROXY_USERNAME
useradd \
    -d /home/$PROXY_USERNAME \
    -m \
    -u $CONTAINER_UID \
    -g $CONTAINER_GID \
    -o \
    $PROXY_USERNAME
gosu $CONTAINER_UID:$CONTAINER_GID /main.sh $@
