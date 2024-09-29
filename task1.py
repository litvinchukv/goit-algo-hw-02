import queue
import random
import time

class ServiceCenter:
    def __init__(self):
        # Створення черги заявок
        self.request_queue = queue.Queue()
        self.request_id = 0

    def generate_request(self):
        # Генерація нової заявки з унікальним номером
        self.request_id += 1
        request = f"Request #{self.request_id}"
        print(f"Generated: {request}")
        # Додавання заявки до черги
        self.request_queue.put(request)

    def process_request(self):
        # Обробка заявки з черги, якщо черга не пуста
        if not self.request_queue.empty():
            request = self.request_queue.get()
            print(f"Processing: {request}")
        else:
            print("No requests to process.")

def main():
    service_center = ServiceCenter()

    # Головний цикл програми
    try:
        while True:
            # Генеруємо нові заявки
            if random.choice([True, False]):
                service_center.generate_request()

            # Обробляємо заявку з черги
            service_center.process_request()

            # Імітуємо невелику затримку
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
