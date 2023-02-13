# Import spacy.
import spacy

# Load model 'en_core_web_md'.
nlp = spacy.load('en_core_web_md')


def main():

    # Assign the description to the variable 'planet_hulk'.    
    planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    
    # Create a token for 'planet_hulk'.
    token_watched = nlp(planet_hulk)

    # Initialize a variable for the list of movies.    
    movie_list = []

    # Read the movies from the file 'movies.txt'.
    with open("movies.txt", "r", encoding="utf-8") as openfile:
        for line in openfile:
            movie_list.append(line.strip("\n"))

    # Initialize a variable for the list of similarities.
    similarities = []    

    # Calculate the similarity between the 'planet_hulk' and the movies in 'movie_list'.
    for movie in movie_list:
        token_new = nlp(movie)
        similarity = token_watched.similarity(token_new)
        
        # Add the similarity to the list 'similarities' in order to find the highest value.
        similarities.append(similarity)

    # Get the highest value.
    highest_score = max(similarities)

    # Get the index of the highest value to use to identify the movie with the highest similarity.
    index_max = similarities.index(highest_score)

    # Get the description of the movie.
    movie_to_watch = movie_list[index_max]

    # Print result.
    print(f"Whith a score of {highest_score:.3f} the movie to watch next is: '{movie_to_watch[:8]}'\nDescription:\n{movie_to_watch[9:]}")


if __name__ == "__main__":
    main()