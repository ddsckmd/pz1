import socket

def scan_ports(target, start_port, end_port):
    print(f"Сканвання {target} на портах з {start_port} до {end_port}...")

    # Перевірка кожного порту в заданому діапазоні
    for port in range(start_port, end_port + 1):
        try:
            # Утворити сокет
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Таймаут для кожної спроби, щоб не зависав сервер

            # Спроба підключитись
            result = sock.connect_ex((target, port))  # 0 = порт відкритий

            if result == 0:
                print(f"Порт {port}: Відкритий")
            else:
                print(f"Порт {port}: Закритий")

            sock.close()  # Закрити сокет, щоб вони не збирались у пам'яті
        except Exception as e:
            print(f"Помилка на порту {port}: {e}")


# В терміналі оце щоб вказати кількість портів для сканування
choice = input(" Для сканування одного порту ввести '1', для сканування діапазону портів ввести '2': ")

if choice == '1':
    target_ip = input("IP-адреса для сканування: ")   # scanme.nmap.org       оце можна сканувати
    single_port = int(input("Порт для сканування: "))
    scan_ports(target_ip, single_port, single_port)  # Сканування вказаного порта

elif choice == '2':
    target_ip = input("IP-адреса для сканування: ") # scanme.nmap.org       оце можна сканувати
    start_port = int(input("Початковий порт: "))
    end_port = int(input("Кінцевий порт: "))
    scan_ports(target_ip, start_port, end_port)  # Сканування вказаного діапазону портів

else:
    print("Невірний вибір! Спробуйте знову.")
