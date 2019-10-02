
class Event:
    all_events = []
    def __init__(self, id, x, y, tickets=[]):
        self.id = id
        self.x = x
        self.y = y
        self.tickets = tickets
        
        if len(tickets) > 0:
            self.all_events.append(self)
            #self.all_events.sort(key=lambda x: (min(x.tickets), x.id))
        
    def buyTicket(self):
        if len(self.tickets) > 0:
            price = min(self.tickets)
            self.tickets.remove(price)
            if len(self.tickets) == 0:
                self.all_events.remove(self)
            return [self.id, price]
        else:
            return [-1, 0]

# The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# Enter your code here. Read input from STDIN. Print output to STDOUT
sizeOfWorld = int(input())

numberOfEvents = int(input())
for i in range(numberOfEvents) :
    eventLine = input()    
    # TODO: you will need to parse and store the events '
    
    temp = eventLine.split(" ")
    
    
    tickets = temp[3:]
    tickets = [int(ticket) for ticket in tickets]
    Event(int(temp[0]), int(temp[1]), int(temp[2]), tickets)

        
    
numberOfBuyers = int(input())
for i in range(numberOfBuyers) :
    buyerLine = input()     
    
    temp = buyerLine.split(" ")
    
    buyerX, buyerY = int(temp[0]), int(temp[1])
    
    assert buyerX >= 0 and buyerX < sizeOfWorld
    assert buyerY >= 0 and buyerY < sizeOfWorld
    
    if len(Event.all_events) > 0:
        event = min(Event.all_events, key=lambda x: (manhattan_distance(buyerX, buyerY, x.x, x.y), min(x.tickets), x.id))
        boughtId, boughtPrice = event.buyTicket()
        print(str(boughtId) + " " + str(boughtPrice))
       
    else:
        print("-1 0")
    
   # print(temp)
    # TODO: you will need to parse and store the buyers 
    
# The solution to the first sample above would be to output the following to console:
# (Obviously, your solution will need to figure out the output and not just hard code it)





        
    
        