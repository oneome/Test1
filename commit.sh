#!/bin/bash
# @author : Pavlov Vladislav

mkdir -p /var/proj/words

mv words.in /var/proj/words/words.in

cd /var/proj/words/

git add words.in
git commit -m "Autocommit words.in | Script run $(date +%Y%m%d)"
git -c credential.helper="!f() { echo username=?; echo password=?; }; f" push