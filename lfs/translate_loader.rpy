#image loader = ("gui/main_menu.png")
init python:
    import renpy.video as video

    # Load the video file
    video_file = "gui/main_menu.mp4"
    main_menu_video = video.load(video_file)

label splashscreen:
    # Create a video channel
    video_channel = renpy.video.VideoChannel()

    # Play the video file on the channel
    video_channel.play(main_menu_video, fadein=1.0)

    label language_chooser:
        menu:
            "English":
                $ persistent.lang = "english"
                $ renpy.change_language("english")

            "Русский":
                $ persistent.lang = "russian"
                $ renpy.change_language("русский")

        # Stop the video when the menu is closed
        video_channel.stop()

    # Wait for the language chooser to finish
    $ renpy.pause(1.0)

    # Continue to the main menu
    jump main_menu

label main_menu:
    # Your main menu code here
