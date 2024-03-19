from playsound import playsound


# you need to install 'playsound' library TO INSTALL -> "pip install playsound"

def sound_decorator(func):
    
    def wrapper(*args, **kwargs):
        try:
            
            result = func(*args, **kwargs)
            print("Chalyoo")
            playsound('nic.mp3')  # Play 'nice.mp3' if function is successful
            return result
        except Exception as e:
            print("Error vayooo")
            playsound('raj.mp3')  # Play 'raj.mp3' if function raises an error
             # Re-raise the exception after playing the sound
    return wrapper



@sound_decorator
def my_function():
    x = 1/2 #which raises error
    
    
    
my_function()