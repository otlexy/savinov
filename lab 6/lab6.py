import lab6func

def main():
    lab6func.test_func()
    data = lab6func.read_data_from_file("input.txt")
    if data is None:
        return
    results = lab6func.process_data(data)
    if lab6func.write_results_to_file("results.txt", results):
        print("Обработка файла завершена. Результаты в 'results.txt'")

if __name__ == "__main__":
    main()
