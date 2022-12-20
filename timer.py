import time
seconds = input("ingresa el tiempo en segundo")

def countdown_timer(seconds):
    while seconds > 0:

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'
        
        print (timer,end='\r')
        time.sleep(1)
        seconds -= 1
    
    print('se acabo el tiempo')
    
countdown_timer(int(seconds))