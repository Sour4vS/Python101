import json

class Movie:
      def __init__(self, movie_id, title, genre, duration, ticket_price, available_seats):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre 
        self.duration = duration
        self.ticket_price = ticket_price
        self.available_seats = available_seats

      def display_details(self):
          return (
               f"ID: {self.movie_id} | "
               f"Title: {self.title} | "
               f"Genre: {self.genre} | "
               f"Duration: {self.duration} mins | "
               f"Price: ₹{self.ticket_price} | "
               f"Seats: {self.available_seats}"
            )
      def book_ticket(self):
          if self.available_seats > 0:
              self.available_seats-=1
              print(f"Ticket booked successfully. Seats left: {self.available_seats}")
          else:
            print("No seats available.")
              
      def cancel_ticket(self):
          self.available_seats +=1
          print("Ticket canceled successfully.")

class MovieManager:
      def __init__(self):
         self.movies = []

      def add_movie(self,movie):
          self.movies.append(movie)

      def display_movies(self):
          for movie in self.movies:
              print(movie.display_details())

      def search_movie(self,movie_id):
          for movie in self.movies:
              if movie.movie_id == movie_id:
                  print(movie.display_details())
                  return
              
          print("Movie doesn't exist..")

      def delete_movie(self,movie_id):
          for movie in self.movies:
               if movie.movie_id == movie_id:
                   self.movies.remove(movie)
                   print("Movie is removed..")
                   return
          print('Movie doesnt exist..')

      def save_data(self):
       try:
          data = []
          for movie in self.movies:
              data.append(movie.__dict__)

          with open("movies.json","w") as file:
              json.dump(data,file,indent = 4)
       except Exception as e:
           print(f"Error while saving data: {e}")
           
      def load_data(self):
          try:
            with open("movies.json", "r") as file:
               data = json.load(file)
               for movie_data in data:
                     movie = Movie(**movie_data)
                     self.movies.append(movie)
            print("Movie data loaded successfully.")
          except FileNotFoundError:
              print("movies.json not found. Starting with an empty movie list.")
              

              
          
m1 = Movie(101,"avengers","action",180,250,100)
m2 = Movie(102,"interstellar","Sci-fi",169,180,80)

moviemanager = MovieManager()
moviemanager.add_movie(m1)
moviemanager.add_movie(m2)
moviemanager.delete_movie(102)
moviemanager.display_movies()
m1.book_ticket()
moviemanager.display_movies()
