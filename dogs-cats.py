def get_names(txt,pet):
    print(f"{pet}'s names:")
    try:
        with open(txt) as pet:
            while True:
                animal = pet.readline()
                if not animal:
                    break
                print(animal.rstrip())
    except FileNotFoundError:
        #print(f"Sorry, the file {txt} doesn't exist!")
        pass

dogs=get_names('dogs.txt','dogs')
cats=get_names('cats.txt','cats')
