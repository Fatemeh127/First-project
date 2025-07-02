import click

@click.group()
def main():
    pass

priorities ={
    "o": "optional",
    "l": "low",
    "h": "high",
    "m": "medium",
    "c": "crucial"
    }
@main.command()
@click.option("--name", prompt="Enter the name", help="the name of file")
@click.option("--description", prompt="describe", help="description")
@click.argument("priority", type=click.Choice(priorities.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt" 
    with open(filename, "a+") as f:
        f.write(f"{name}: {description}[priority: {priorities[priority]}]\n")

@main.command()
@click.argument("idx", type=int, required=1)
def delete_todo(idx):
    with open("mytodos.txt", "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt", "w") as f:
        f.write("\n".join(todo_list))
        f.write('\n')

@main.command()
@click.option("--priority", "-p", type=click.Choice(priorities.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            click.echo(f"({idx}) - {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[priority: {priorities[priority]}]" in todo:
                click.echo(f"({idx}) - {todo}")

                

if __name__ == "__main__":
    main()
        
