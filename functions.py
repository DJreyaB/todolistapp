def get_todos(file_path="todos.txt"):
    with open(file_path, "r") as local_file:
        all_todos = local_file.readlines()
    return all_todos

def write_todos(todos_arg, file_path="todos.txt"):
    with open(file_path, "w") as local_file:
        local_file.write(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

