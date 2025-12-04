import lab6func

def main():
    data = lab6func.read_data_from_file("input.txt")
    if data is None:
        print("Не удалось прочитать данные из файла.")
        return

    results = lab6func.process_data(data)
    
    if lab6func.write_results_to_file("results.txt", results):
        print("Обработка файла завершена. Результаты в 'results.txt'")
    else:
        print("Ошибка при записи результатов в файл")

if __name__ == "__main__":
    main()
