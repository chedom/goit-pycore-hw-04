def calculate_total_salary(path: str) -> tuple[int, float]:
    total_employees = 0
    total_sum = 0

    with open(path, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line: # end of file
                break

            parts = line.split(',')
            if len(parts) < 2: # line doesnt satisfy expected format
                print(f"Line {line} has unexpected format")
                continue

            try:
                total_sum = total_sum + int(parts[1])
                total_employees = total_employees + 1
            except ValueError:
                print(f"Expected int, got {parts[1]}")
                continue

    return (total_sum, total_sum//total_employees) # returns intentionally int for average salary

# wrapper for calculate_total_salary to handle exceptions
def total_salary(path: str) -> tuple[int, float]: 
    try:
        return calculate_total_salary(path)
    except FileNotFoundError:
        print(f"File {path} not found, check if the file exists and the path is correct")
        return (0, 0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return (0, 0)

# example of usage
total, average = total_salary('./01_task/salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# file not found
total, average = total_salary('./01_task/salary_file_not_found.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
