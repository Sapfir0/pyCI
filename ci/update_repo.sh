#!/bin/bash

source helper.sh
rm -f .commit_hash

helper "repo dir not found" pushhd $1 1> /dev/null
helper "cant reset git" git reset --hard HEAD

COMMIT=$(helper "cant call 'git log' on repo" git log -n1)
if ($? != 0); then
    echo "cant call 'git log' on repo"
    exit 1
fi

HASH=`echo $COMMIT | awk '{ print $2}'`
helper "cant pull from repo" git pull

COMMIT=$(helper "cant call 'git log' on repo" git log -n1)
if ($? != 0); then
    echo "cant call 'git log' on repo"
    exit 1
fi

NEWHASH=`echo $COMMIT | awk '{ print $2}'`

if [$NEWHASH != $HASH]; then
    popd 1> /dev/null
    echo $NEWHASH > .commit_hash
fi