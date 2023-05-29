#!/bin/bash
#
# Ejemplo de Menu en BASH
# Script SuperScant
# <7/03/2023> <Aaron Avila Mata>
#
date
    echo "|"
    echo "|---------------------------|"
    echo "|   Menu Principal          |"
    echo "|---------------------------|"
    echo "|1. Net Discover"
    echo "|2. Portscan"
    echo "|3. Welcome"
    echo "|4. Exit"
    echo "|"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) /home/dearwinner1/Tarea5/netdiscover.sh;;
        2) /home/dearwinner1/Tarea5/portscan.sh;;
        3) /home/dearwinner1/Tarea5/welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac
