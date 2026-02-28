#Day 25 - Todo List
todos = []

todos.append("Learn Python")
todos.append("Git commit")
todos.append("Job apply")

print("My todos:")
for i, task in enumerate(todos, 1):
    print(f"{i}. {task}")
