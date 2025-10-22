def parse_cat_info(raw_line: str) -> object: 
    [id_val, name, age] = raw_line.strip().split(',')

    return {"id": id_val, "name": name, "age": age}


def get_cats_info(path: str) -> list[object] | None:
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line: # end of file
                    break

                cats_info.append(parse_cat_info(line))
           
            return cats_info
    except FileNotFoundError:
        print(f"File {path} not found, check if the file exists and the path is correct")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# example
cats_info = get_cats_info("./02_task/cats_file.txt")
print(cats_info)
# file not found
cats_info = get_cats_info("./02_task/not_found.txt")
print(cats_info)