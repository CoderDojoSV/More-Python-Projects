## The Mouse

Most of the games we've made so far have let the user use the keyboard to tell the games what they want to do. Today, we're going to take a look at using the mouse!

You can get the position of the mouse pointer and whether or not the mouse buttons are pressed down using:

    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    (left_button_pressed, middle_button_pressed, right_button_pressed) = pygame.mouse.get_pressed()

### Challenge 1

Using the enclosed "blank pygame project.py", write a program to draw a little circle right under the mouse cursor.

### Challenge 2

Make a drawing program! Whenever the mouse button is being pressed down, draw something where the mouse cursor is.

*Tip:* It might be useful to remove the `screen.fill(black)` line for this one.

## Mouse Events

Knowing where the mouse is is fine and dandy, but what if you want to know the moment the user clicks the mouse? To do this, we can use **events**, just like we did for the keyboard.

    for event in pygame.event.get():
        #... more events here...
        if event.type == pygame.MOUSEBUTTONDOWN:
            # The mouse button got clicked down.
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            # The mouse button stopped being clicked down.
            pass

### Challenge 3

Make a program that plays a sound when you click on it. You can use one of the sounds from last week or find/make your own!

### Challenge 4

Make a "soundboard" -- a program that can play several different sounds depending on where the user clicks. You can use some of the sounds from last week or find/make your own. You might also want to draw some shapes on the screen to show where the user can click to play a sound.

## Fun Additional Challenges

Done with everything else? Here are some more things to try! You might need to use the [Pygame documentation](http://www.pygame.org/docs/index.html) for some of these.

### Challenge 5

Make a game where you have to move the mouse around to dodge objects flying around the screen.

### Challenge 6

Make a game where you have to try and click on something as many times as possible in 5 seconds.