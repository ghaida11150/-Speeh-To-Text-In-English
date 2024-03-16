import speech_recognition as sr

def speech_to_text():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Speak now...")

        # Adjust for ambient noise before listening
        recognizer.adjust_for_ambient_noise(source)

        # Continuously listen for speech and convert to text
        while True:
            audio = recognizer.listen(source)

            try:
                # Recognize speech using the default API (PocketSphinx)
                text = recognizer.recognize_sphinx(audio)
                print("You said:", text)

                # Write the recognized text to a text file
                with open("output.txt", "a") as file:
                    file.write("You said: " + text + "\n")
            except sr.UnknownValueError:
                print("Waiting for speech...")
            except sr.RequestError as e:
                print("Error: {0}".format(e))

# Call the function to start live speech recognition
speech_to_text()