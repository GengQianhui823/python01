def todo_list():
    tasks = []  # 存储任务的列表

    while True:
        print("\n任务清单管理系统")
        print("1. 添加任务")
        print("2. 删除任务")
        print("3. 显示任务")
        print("4. 退出系统")


        choice = input("请选择操作(1-4): ")

        if choice == "1":
            # 添加任务
            task = input("请输入新任务内容: ")
            tasks.append(task)
            print(f"任务 '{task}' 已添加!")

        elif choice == "2":
            # 删除任务
            if not tasks:
                print("任务清单为空!")
                continue

            print("\n当前任务清单:")
            display_tasks(tasks)

            try:
                num = int(input("\n请输入要删除的任务编号: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"任务 '{removed}' 已删除!")
                else:
                    print("编号无效!")
            except ValueError:
                print("请输入有效的数字编号!")

        elif choice == "3":
            # 显示任务
            if not tasks:
                print("任务清单为空!")
            else:
                print("\n当前任务清单:")
                display_tasks(tasks)

        elif choice == "4":
            # 退出系统
            print("感谢使用任务清单系统!")
            break

        else:
            print("无效的选择，请重新输入!")


def display_tasks(tasks):
    """显示当前所有任务并添加编号"""
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


if __name__ == "__main__":
    todo_list()