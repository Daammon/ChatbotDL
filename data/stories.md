## find actor movies happy path
* greet
  - utter_greet
* find_actor_movies{"actor":["Brus Uilis"]}
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


## find actors coincidence in movies
* greet
  - utter_greet
* find_actors_coincidence_in_movies{"actor":["Brus Uilis", "Arnold chuache"]}
  - action_find_actors_coincidence_in_movies
  - slot{"movie":"Los intocables"}
* thanks
  - utter_goodbye

## find movie rankings by genre
* greet
  - utter_greet
* find_movie_rankings_by_genre{"genre":"action"}
  - action_find_movie_rankings_by_genre
  - slot{"ranking":"Terminator, La jungla de Cristal, Alien"}
* thanks
  - utter_goodbye

## find movie rankings by actor
* greet
  - utter_greet
* find_movie_rankings_by_actor{"actor":"Bruce Willis"}
  - action_find_movie_rankings_by_actor
  - slot{"ranking":"La jungla de Cristal, Pulp Fiction, Four rooms"}
* thanks
  - utter_goodbye
  
  
## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
