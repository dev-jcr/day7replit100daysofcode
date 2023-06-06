#Fake fan question generator. Nesting if statements
music = input("What is your favorite music artist? ")
if music != "Radiohead":
  print("Ugh, why? <3")
else:
  fsong = input("Which is your favorite song? ")
  if fsong == "lotus flower" or fsong == "Lotus Flower":
    print("That or Nude")
    slyric = input("Do you know the first phrase of the song?")
    if slyric == "yes":
      print("I will shake myself into your pocket...")
      complete = input("Do you know what goes next in the song?")
      if complete == "no":
        print("We neither!")  
      else:
          print("""

          Invisible
          Do what you want
          Do what you want
          
          """)
          falbum = input("Favorite Radiohead album?")
          if falbum == "In Rainbows" or falbum == "in rainbows":
            print("It's the best of all times")
          elif falbum == "Kid A" or "kid a":
            print("Love it!")
          else:
           print("Not my fav, but all of Radiohead is great")