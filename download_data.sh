#!/usr/bin/env bash

# download and extract the data if absent
if [ ! -f p2p-Gnutella31.txt.gz ];
then
    curl http://snap.stanford.edu/data/p2p-Gnutella31.txt.gz | gunzip > p2p-Gnutella31.txt
fi

# extract the data if absent
if [ ! -f p2p-Gnutella31.txt ];
then
    gunzip p2p-Gnutella31.txt
fi

# prepare truncated data if absent
if [ ! -f p2p-Gnutella31.truncated.txt ];
then
    head -10000 p2p-Gnutella31.txt > p2p-Gnutella31.truncated.txt
fi
