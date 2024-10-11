import subprocess

print("1 - полный скан nmap\n2 - скан уязвимостей nmap\n3 - DOS атакка\nТОЛЬКО Kali! 4 - Поиск информации\nТОЛЬКО Kali! 5 - скан web уязвимостей\nТОЛЬКО Kali! 6 - подмена ссылки (beta)")
print("ТОЛЬКО kali! 7 - брутфорс wifi (beta\n)")

choice = int(input("Выберите скрипт для выполнения: "))

if choice == 1:
    open_nmap_script("nmap_full.sh")
elif choice == 2:
    open_nmap_script("nmap_vuln.sh")
elif choice == 3:
    subprocess.run(["python3", "data/dos.py"], check=True)
elif choice == 4:
    subprocess.run(["bash","data/recon.sh"], check=True)
elif choice == 5:
    subprocess.run(["bash", "data/web_vuln.sh"], check=True)
elif choice == 6:
    subprocess.run(['python3', 'data/packet_take.py'], check=True)
elif choice == 7:
    subprocess.run(["bash", "data/wifi.sh"], check=True)



else:
    print("Неверный выбор.")
