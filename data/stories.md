## find actor movies happy path
* greet
  - utter_greet
* find_actor_movies{"actor":"Bruce Willis"}
  - action_find_actor_movies
  - slot{"movie":"Die Hard"}
* thanks
  - utter_goodbye
  
## find movie release date
* greet
  - utter_greet
* find_movie_release_date{"movie":"Die Hard"}
  - action_find_movie_release_date
  - slot{"releaseDate":"1989"}
* thanks
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
