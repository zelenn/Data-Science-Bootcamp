import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
           'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
           'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']


def call_center():
    return list(set(clients) - set(recipients))

def potential_clients():
    return list(set(participants) - set(clients))

def loyalty_program():
    return list(set(clients) - set(participants))

def marketing(task):
    if task == "call_center":
        return call_center()
    elif task == "potential_clients":
        return potential_clients()
    elif task == "loyalty_program":
        return loyalty_program()
    else:
        raise Exception("Invalid task")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        sys.exit()
    result = marketing(sys.argv[1])
    for email in result:
        print(email)