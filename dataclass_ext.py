from dataclasses import dataclass

@dataclass
class Shows:
    title:str
    rating:float
    episodes:int
    
    def display_info(self):
        return f"Title: {self.title}, Rating: {self.rating}, Episodes: {self.episodes}"

def main():
    shows=[
        #Rating are from IMDB
        Shows("One Piece", 9.0, 1092),
        Shows("Dragon Ball Z", 8.8, 291),
        Shows("Bleach", 8.2, 366)
    ]
    shows.append(Shows("Naruto", 8.7, 500))
    
    #Prints the first show on the list
    print(shows[0])
    
    #Executes loop to print the data
    #The function is created on line 10
    for show in shows:
        print(show.display_info())
        
        
if __name__ == "__main__":
    main()
    
    