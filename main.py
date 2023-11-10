star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

# Ask the user for the number of the trilogy
trilogy_number = int(input("Enter the number of the trilogy (1, 2 or 3): "))

# Ask the user for the number of the film in the trilogy
film_number = int(input("Enter the number of the film in the trilogy (1, 2 or 3): "))

if 1 <= trilogy_number <= 3 and 1 <= film_number <= 3:
    # Print the title of the film corresponding to the user selection
    film_title = star_wars_movies[trilogy_number - 1][film_number - 1]
    print("The title of the movie is:", film_title)
else:
    print("This is not the movie you are looking for.")
