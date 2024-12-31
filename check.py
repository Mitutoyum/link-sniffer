# check for valid links and remove duplicates, invalid


def check():
    with open("records.txt", "r+", encoding="utf-8") as file:
        content = file.readlines()
        content = list(dict.fromkeys(content))

        file.seek(0)
        file.truncate()
        file.writelines(content)


if __name__ == "__main__":
    check()
