## Sounds!

In Beginner Python, you made a couple of cool games! There's one problem, though: they were completely silent! Today, we're going to learn about making sounds in Python!

Pygame includes a module called `pygame.mixer` that lets us play sounds. But first, we need a sound to play!

    kerblammo = pygame.mixer.Sound("kerblammo.wav")

Once we have a sound, we can press "Play" on it at the appropriate moment:

    if alien_spacecraft.just_got_blown_up:
        kerblammo.play()

### Challenge 1: Pong With Sounds

Take the Pong game from Beginner Python and add some sounds to it! If you don't have your Pong code any more, [here is a complete game](https://raw.githubusercontent.com/CoderDojoSV/beginner-python/master/Day-6/finished/pong%20finished.py) you can use. 

We've included a couple sound files for you to use, which you can download by clicking on them, right-clicking "Raw", and choosing "Save link as...". Put them in the same folder as your program.

### Challenge 2: Pong With Your Own Sounds

The sounds we gave you were boring. Record your own (with Audacity or another program) or download them from a website like [Freesound](https://www.freesound.org/)!

## Music!

Now that we've added sound to our games, it's time for the second step: a cool soundtrack! Pygame gives us `pygame.mixer.music`, which we can use to stream in some music.

    pygame.mixer.music.load("DiscoMonkeysInSpace_soundtrack.mp3")
    pygame.mixer.music.play(-1) #-1 means repeat the music forever

One other thing you should know is how to set the volume. If you want a particular sound effect to be much louder than the music, you can try:

    pygame.mixer.music.set_volume(0.5) # half volume
    kerblammo.set_volume(1.0) #MAXIMUM VOLUME!!!!!!

### Challenge 3: Pong with Music

Add some music to your Pong game! We've given you a track to use, but you can also try and download (or make) your own!

## Fun Additional Challenges

Done with everything else? Here are some more things to try! You might need to use the [`pygame.mixer` documentation](http://pygame.org/docs/ref/mixer.html#pygame.mixer.Sound) to figure some things out yourself.

###Challenge 4: A Unique Sound for Everything

Can you have a different sound for everything that happens in your game: the ball hitting paddle 1, the ball hitting paddle 2, scoring a point, the game starting, the game ending, etc. Get creative!

### Challenge 5: Fading Out

Make the music fade out at when you close the Pong window!

### Challenge 6: Patatap

Try and make something like [this](http://www.patatap.com/) in Python.
