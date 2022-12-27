def hi(lang, name):

    if lang=="en":
        print(f"Hello, {name}!")
    elif lang=="ro":
        print(f"Salut, {name}!")
    elif lang=="ru":
        print(f"Privet, {name}!")


hi("en", "john")
hi("ro", "Ion")
hi("ru", "Dima")