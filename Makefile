all: data

data: p2p-Gnutella31.txt
	curl http://snap.stanford.edu/data/p2p-Gnutella31.txt.gz | gunzip > p2p-Gnutella31.txt
