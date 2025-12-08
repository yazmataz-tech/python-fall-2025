
#song list project <3


# just the title teehee
playlist = ["POOKIE'S REQUIEM", "Stateside", "Swan Lake", "Use Your Heart"]

#  Let viewer choose the playlist name
playlist_name = input("What should we name the playlist? ")

print("---", playlist_name, "---")
print("These are the songs were working with so far:")
print(playlist)

# Ask if the viewer wants to put in new songs
add_choice = input("Hi, this is the class playlist! Want to add your own touch? (yes/no): ")

if add_choice.lower() != "yes":
    print("Come back next time!...i see how it is...")
else:
    # Adding songs
    song1 = input("What is your first pick ?: ")
    playlist.append(song1)

    # Ask if they want to add a second song
    add_second = input("Do you want to add another song? (yes/no): ")
    if add_second.lower() == "yes":
        song2 = input("Okay, what is the song ?: ")
        playlist.append(song2)

    # Removing songs
    remove_choice = input("Do you want to remove a song? (yes/no): ")

    if remove_choice.lower() == "yes":
        print("Okay, update, this is the playlist now.:")
        print(playlist)
        song_remove = input("Which song would you like to remove? be specific...that means NO typos.. P.S..i see how it is...you don't like my music, huh?...: ")

        # Only remove if the song is in the list OR ELSE IT DOESNT WORKKKK
        if song_remove in playlist:
            playlist.remove(song_remove)
        else:
            print("That song is not in the playlist,... maybe it's a spelling error")

# Final playlist and ending message
print("YAYYY FINAL PLAY LIST")
print(playlist)
print("Thank you for your choices! These are great songs. Come back soon!")
print("P.S reset this program when you're done please,")