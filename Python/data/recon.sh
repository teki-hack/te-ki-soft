#!/bin/bash
    
    
read -p 'введи ip сканируемого хоста' domain

echo "Сбор информации о домене: $domain"
whois $domain
dig $domain any
nslookup $domain
theHarvester -d $domain -b all