pusher_x = 1
pusher_y = 0

##box_x = 1
##box_y = 2
##
box={
    "x": 4,
    "y": 2
    }
box2={
    "x": 2,
    "y": 4
    }
boxes=[
    {
    "x": 1,
    "y": 2
    },
    {
    "x": 2,
    "y": 4
    }   
    ]


##dest_x = 3
##dest_y = 2

dest=[
    {
    "x": 3,
    "y": 2
    
    },
    {
    "x": 5,
    "y": 4
    }
    ]

size_x = 6
size_y =6

def check_win(boxes, dest):
    win = 0
    for box in boxes:
        for des in dest:
            if box["x"] == des["x"] and box["y"] == des["y"]:
                win += 1
    return win

def check(x, y, boxes):
    for box in boxes:
        if x == box["x"] and y == box["y"]:
            return True
    return False

def check_overlap(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False
    

def is_in_map(x, y, size_x, size_y):
    return 0 <= x < size_x and 0 <= y < size_y
 
    
def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":    
        dy -= 1
    elif direction == "A":
        dx -= 1
    elif direction == "S":
        dy += 1
    elif direction == "D":
        dx += 1
    else:
        print("You enter wrong button pls do this again beo:)")
    return dx, dy
        
def print_map(size_x, size_y, pusher_x, pusher_y, boxes):
    for y in range(size_y):
        for x in range(size_x):
            if x == pusher_x and y == pusher_y:
                print(" P ", end="")
            elif check_overlap(x, y, boxes):
                print(" B ", end="")
            elif check_overlap(x, y, dest):
                print(" D ", end="")
            else:
                print(" - ", end="")
        print()
        
# main GAME_LOOP

while True:
    print_map(size_x, size_y, pusher_x, pusher_y, boxes)
    direction = input("What is your next move:(W/A/S/D) ").upper()
    
    ## xu ly dau vao
    
    dx, dy = input_process(direction)
    if box["x"] == pusher_x and box["y"] == pusher_y:
        if is_in_map(box["x"] + dx, box["y"] + dx, size_x, size_y):
            if box["x"] + dx != box2["x"] and box["y"] != box2["y"]:
                box["x"] += dx
                box["y"] += dy
                pusher_x += dx
                pusher_y +=dy
            else:
                print("you can push bro:")
        else:
            print("Pass")
    elif box2["x"] == pusher_x and box2["y"] == pusher_y:
        if is_in_map(box2["x"] + dx, box2["y"] + dx, size_x, size_y):
            if box["x"] + dx != box2["x"] and box["y"] != box2["y"]:
                box2["x"] += dx
                box2["y"] += dy
                pusher_x += dx
                
                pusher_y += dy
            else:
                print("You can push")
        else:
            print("Waitting")
    else:
        next_pusher_x=pusher_x+dx
        next_pusher_y=pusher_y+dy
        if(is_in_map(pusher_x+dx,next_pusher_y,size_x,size_y)):
                
            pusher_x += dx
            pusher_y += dy
        else:
            print("you can move")

    win=check_win(boxes,dest)
    if win == len(dest):
       print(print_map(size_x, size_y, pusher_x, pusher_y, boxes))
       print(" Victory")

       break

        
                

















##        for box in boxes:
##            if pusher_x + dx == box["x"] and pusher_y + dy == box["y"]:
##                if check(box["x"] + dx, box["y"] + dy, boxes):
##                    print("You can")
##                else:
##                    if is_in_map(box["x"] + dx, box["y"] + dy, size_x, size_y):
##                        if is_in_map(pusher_x + dx, pusher_y + dy, size_x, size_y):
##                            
####        if is_in_map(box["x"] + dx, box["y"] + dy, size_x, size_y):
##        #truoc mat la hop
##
##                            box["x"] += dx
##                            box["y"] += dy
##                            
##                            # cho thang hop di chuyen
##                            
##                            pusher_x += dx
##                            pusher_y += dy
##                    
##            # cho thang day hop di chuyen
##        else:
##            print("You can't push bro")
##    
##    else:
##        if is_in_map(pusher_x + dx, pusher_y + dy, size_x, size_y):
##            
##            pusher_x += dx
##            pusher_y += dy
##
##    if check_overlap(pusher_x + dx, pusher_y + dy, boxes):
##        for box in boxes:
##            for des in dest:
##                if box["x"] == dest["x"] and box["y"] == dest["y"]:
##                    print_map(size_x, size_y, boxes, pusher_x, pusher_y, dest)
##                    print(" victory")
##                    
##                break
            
        

    

    
