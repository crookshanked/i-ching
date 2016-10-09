#!/bin/zsh

for i in `seq 1 64`; 
do
  curl -s "http://deoxy.org/iching/$i" | pup 'pre' > /Users/briankustra/data/iching/chapter-"$i"
done
