#!/bin/bash

read -p "введи ip/имя хоста: " url
echo 'сканирование началось...'
nikto -h $url