

#creating the list of movies 
movies=[]

#function to add movie
def add_movie():
    n = int(input("enter the number of movies you want to add: "))
    #input of the dictionary into a list as an element 
    for i in range(0,n):
        raw_name=input("name: ")
        raw_director=input("director: ")
        Year=input("year: ")
        Name=raw_name.title()
        Director=raw_director.title()
        movie={
            "Name":Name,
            "Director":Director,
            "Year":Year
        }
        movies.append(movie)


#function to view movie
def view_movie(movie_list):
    for movie in movie_list:
        print(f"Name:{movie['Name']}")

    raw_user_input=input("press M to view more details or Q to end: ")
    user_input=raw_user_input.upper()
    while user_input!='Q':
        if user_input=='M':
            for movie in movie_list:
                print(f"Name:{movie['Name']}")
                print(f"Director:{movie['Director']}")
                print(f"released year:{movie['Year']}")
        elif user_input=='Q':
            print("you have terminated the process")

        else:
            print("you have given the wrong command ")

        raw_user_input = input("press M to view more details or Q to end: ")
        user_input = raw_user_input.upper()


#function to search movie
def search_movie():
    raw_find_by=input("enter by which property you want to search: ")
    find_by=raw_find_by.title()
    raw_looking_for = input("what are you searching: ")
    looking_for=raw_looking_for.title()
    found_movie=search_by_attribute(movies,looking_for,lambda x: x[find_by])

    view_movie(found_movie)


def search_by_attribute(movies,expected,finder,raw_error):
    found=[]
    for i in movies:
        if finder(i)==expected:
            found.append(i)

    return found


#main menu option
def menu():
    raw_user_input = input("press A to add movie, press V to view your movies, press S to search movie, press Q to quit: ")
    user_input=raw_user_input.title()
    while user_input!='Q':

        if user_input=='A':
            add_movie()
        elif user_input=='V':
            view_movie(movies)
        elif user_input=='S':
            search_movie()
        elif user_input=='Q':
            print("project close....back to the home! ")
        else:
            print("you have given wrong command, please check!!!!")
        raw_user_input = input("press A to add movie, press V to view your movies, press S to search movie, press Q to quit: ")
        user_input = raw_user_input.title()

#calling the menu 
menu()




