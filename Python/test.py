import subprocess

def open_nmap_script(script_name):
    try:
        subprocess.run(["bash", f"data/{script_name}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении скрипта {script_name}: {e}")

print("1 - Запустить nmap_full.sh\n2 - Запустить nmap_vuln.sh\n3 - DO>
choice = int(input("Выберите скрипт для выполнения: "))

if choice == 1:
    open_nmap_script("nmap_full.sh")
elif choice == 2:
    open_nmap_script("nmap_vuln.sh")
elif choice == 3:
    # Запускаем dos.py как скрипт
    subprocess.run(["python", "data/dos.py"], check=True)
else:
    print("Неверный выбор.")

