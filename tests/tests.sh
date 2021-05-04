#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'

make re -sC ../

./../109titration values.csv > got
echo $? >> got

diff result got

if [[ $? == 0 ]]
then
    echo -e "${GREEN}OK${NOCOLOR}"
else
    echo -e "${RED}KO${NOCOLOR}"
fi

rm got
