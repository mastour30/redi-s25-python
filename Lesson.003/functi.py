def display_movies():
    movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    print("Available movies:")
    for movie in movies:
        print(movie)
    return movies

def book_tickets(movies):
    chosen_movie = input("Enter the movie you want to watch: ")

    if chosen_movie in movies:
        seat = int(input("Enter the number of tickets: "))
        total_cost = seat * 12
        print(f"Your total cost: {total_cost}€")
    else:
        print("Sorry, that movie is not available.")

def main():
    movies = display_movies()
    book_tickets(movies)

if __name__ == "__main__":
    main()
