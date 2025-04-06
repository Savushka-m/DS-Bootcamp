import sys

class CustomException(Exception):
    pass
    
def decide(arg):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    set_clients = set(clients)
    set_participants = set(participants)
    set_recipients = set(recipients)
    if arg == "call_center":
        print(list(call_center(set_clients, set_recipients)))
    elif arg == "potential_clients":
        print(list(call_center(set_clients, set_participants)))
    elif arg == "loyalty_program":
        print(list(call_center(set_clients, set_participants)))
    else:
        raise CustomException((f"Wrong task name - {arg}"))


def call_center(set_clients, set_recipients):
    return list(set_clients - set_recipients)

def potential_clients(set_clients, set_participants):
    return list(set_participants - set_clients)

def loyalty_program(set_clients, set_participants):
    return list(set_clients - set_participants)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        decide(arg)