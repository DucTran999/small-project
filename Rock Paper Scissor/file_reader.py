"""The file reader module provides functions for handling read files."""


def read_file_txt(filepath) -> None:
    try:  # If the reading file has a problem, it will not crash the program.
        with open(filepath, mode="r") as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        err_msg = "<!> Some problems have occured while loading file!"
        help_msg = (
            "\n<?> Help: You can change your current working directory"
            " to small_project and restart the game. \nIt might solve "
            "the problem or you can enter keyword 'gameplay' to see it."
            "\n<T.T> Sorry, about this inconvenience."
        )
        print(err_msg, help_msg)
    else:
        print(contents)
