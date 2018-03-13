#MasonWhiteFeburary2018
#Program That Users enter a Review into.

print ("Hello! To review your subject please answer the following; ")

review_material = []

movies = []
musics = []
arts = []
literature = []

media_type = input("What is the media type?: ")
review_material.append(media_type)

genre = input("What is the genre?: ")
review_material.append(genre)

title = input("What is the title?: ")
review_material.append(title)

year = input("What year was it created?: ")
review_material.append(year)

description = input("Short Desscription: ")
review_material.append(description)

rating = float(input("Please Rate it from 0-10, you can use decimals if necessary: "))
review_material.append(rating)

valid = ["Movie", "Song", "Art", "Literature"]

if media_type == ("Movie") or media_type == ("movie") or media_type == ("Film") or media_type == ("film"):
    valid.append(media_type)
    movies.append(review_material)
    print (movies[0:])
    
if media_type == ("Song") or media_type == ("song") or media_type == ("music") or media_type == ("Music"):
    valid.append(media_type)
    musics.append(review_material)
    print (musics[0])
    
if media_type == ("Art") or media_type == ("art") or media_type == ("Painting") or media_type == ("painting") or media_type == ("Picture") or media_type == ("picture") or media_type == ("Drawling") or media_type == ("drawling"):
    valid.append(media_type)
    arts.append(review_material)
    print (arts[0:])
    
if media_type == ("Literature") or media_type == ("literature") or media_type == ("Book") or media_type == ("book"):
    valid.append(media_type)
    literature.append(review_material)
    print (literature[0:])

if media_type not in valid:
    print("That type of media isn't on our records!.")
 





 



