command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start a car
stop - to stop a car
quit - to 
         """)
    elif command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started ")    
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")  
        
    elif command == "quit":
        break
    else:
        print("I don't understand...")                 
