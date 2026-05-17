def say_hello(name):
    message = "Hello, " + name + "!"
    return message

greetings = say_hello("Python learner")
print(greetings)

def check_status(status):
    if status["is_server_running"] == True:
        return "Server is running on port " + status["port"]
    else:
        return "Server is not running."
    
server_status = {"is_server_running": False, "port": "8080"}
print(check_status(server_status))

