import unitary_operator
from ssg.site import site

def main(source="content", dest ="dist"):
    config = {"source": source, "dest": dest}

    Site(**config).build()

typer.run(main)
