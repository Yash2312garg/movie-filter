

movies=[]
def add_movie():
    n = int(input("enter the number of movies you want to add: "))
    for i in range(0,n):
        name=input("name: ")
        director=input("director: ")
        year=input("year: ")
        movie={
            "name":name,
            "director":director,
            "year":year
        }
        movies.append(movie)


def view_movie(movie_list):
    for movie in movie_list:
        print(f"name:{movie['name']}")

    user_input=input("press M to view more details or Q to end: ")
    while user_input!='Q':
        if user_input=='M':
            for movie in movie_list:
                print(f"name:{movie['name']}")
                print(f"director:{movie['director']}")
                print(f"released year:{movie['year']}")
        elif user_input=='Q':
            print("you have terminated the process")
        else:
            print("you have given the wrong command ")
        user_input = input("press M to view more details or Q to end: ")



def search_movie():
    find_by=input("enter by which property you want to search: ")
    looking_for = input("what are you searching: ")
    found_movie=search_by_attribute(movies,looking_for,lambda x: x[find_by])

    view_movie(found_movie)


def search_by_attribute(movies,expected,finder):
    found=[]
    for i in movies:
        if finder(i)==expected:
            found.append(i)
    return found


def menu():
    user_input = input("press A to add movie, press V to view your movies, press S to search movie, press Q to quit: ")
    while user_input!='Q':

        if user_input=='A':
            add_movie()
        elif user_input=='V':
            view_movie(movies)
        elif user_input=='S':
            search_movie()
        elif user_input=='Q':
            print("project close....back to the home! ")
        user_input = input("press A to add movie, press V to view your movies, press S to search movie, press Q to quit: ")
menu()







