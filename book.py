import click

@click.group()
def main():
    pass
genres = {
    "f": "Fiction",
    "nf": "Non-Fiction",
    "s": "Sci-Fi",
    "b": "Biography",
    "m": "Mystery"
}
@main.command()
@click.option('--name','-n', prompt="Enter the name of book", help="The name of book")
@click.option('--author','-a',prompt="Enter the name of author", help="The name of author")
@click.argument("genre", type=click.Choice(genres.keys()), default="f")
@click.argument("bookfile", type=click.Path(exists=False),required=False)             
def add_book(name,author,genre,bookfile):
    filename = bookfile if bookfile is not None else "mybook.txt"
    with open(filename, "a+") as f:
        f.write(f"{name} by {author} [Genre: {genres[genre]}]\n")
    


@main.command()
@click.argument("idx", type=int, required=1)
def delete_bookidx(idx):
    with open("mybook.txt", "r") as f:
        book_list=f.read().splitlines()
        book_list.pop(idx)
        
    with open("mybook.txt", "w") as f:
        f.write("\n".join(book_list))
        f.write('\n')


@main.command()
@click.option('--bookname', '-b', prompt="Enter the name of book", help="Write the name")
@click.argument("bookfile", type=click.Path(exists=True),required=False)
def delete_bookname(bookname, bookfile):
    filename = bookfile if bookfile is not None else "mybook.txt"
    with open(filename, "r") as f:
        book_list = f.read().splitlines()
        new_list = [book for book in book_list if bookname not in book]

    with open("mybook.txt", "w") as f:
        f.write("\n".join(new_list))
        f.write('\n')
        
        
@main.command()
@click.argument("genre", type=click.Choice(genres.keys()), default="f")
@click.argument("bookfile", type=click.Path(exists=False),required=False)
def list_book(genre, bookfile):
    filename = bookfile if bookfile is not None else "mybook.txt"
    with open(filename, "r") as f:
        book_list = f.read().splitlines()
    if genres is None:
        for idx, book in enumerate(book_list):
            click.echo(f"({idx}) - {book}")

    else:
        for idx, book in enumerate(book_list):
            if f"[Genre: {genres[genre]}]" in book:
                click.echo(f"({idx}) - {book}")
            


if __name__ == '__main__':
    main()
