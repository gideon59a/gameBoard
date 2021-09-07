from db_if.db_models import *

def db_models_test():
    bb = BoardG4inRow()
    print(f'pure bb type and value: {type(bb)} {bb}')
    print(f'type and value: {type(bb.__dict__)} {bb.__dict__}')
    b1 = json.loads(json.dumps(bb.__dict__))
    b2 = str(bb.__dict__)
    print(f'b1 {type(b1)} {b1}')
    print(f'b2  {type(b2)} {b2}')

    new_room = Room(board=b2)
    room_dict = new_room.__dict__
    print(f'new room dict: {new_room.__dict__}')
    room_id = 100
    room_dict["id"] = room_id
    print(f'modified room_dict {room_dict}')

    num_cols = 7
    num_rows = 8
    board0 = BoardG4inRow(
                          player="A",  # A or B
                          winner="",  # equals to A, B, Tie, or null ** Note: Common to other games too **
                          matrix=[["-" for _ in range(num_cols)] for _ in range(num_rows)],  # martix[row][column]
                          next_row=[0 for i in range(num_cols)],  # init the next row available for each col,
                          last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                          last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                          last_player=" ")

    # The below example is not useful - see room2
    room1 = Room(id=1,
                game_type="G4inRow",
                room_status=0,
                player_1_id=1,
                player_2_id=2,
                board=json.loads(json.dumps(board0.__dict__)))  # no point to use the json here

    room2 = Room(id=1,
                 game_type="G4inRow",
                 room_status=2,
                 player_1_id=21,
                 player_2_id=22,
                 board=str(board0.__dict__))   # Previously dict was used.

    print(type(room1), room1.__str__())  # Returns the whole class, but NOT as a dict

    print("------BOARD0----------")
    print(type(board0.__dict__), board0.__dict__)  # The class DICT !
    print(f'{type(json.dumps(board0.__dict__))}, {json.dumps(board0.__dict__)}')  # The class default __str__
    print(f'matrix: {board0.__dict__["matrix"]}')  # Printing an item from the dict, the matrix.

    print("-----ROOM1-----------")
    print(type(room1.__dict__), room1.__dict__)
    print(type(json.dumps(room1.__dict__)), json.dumps(room1.__dict__))

    # In the code the dict will be used
    my_room_dict = room1.__dict__
    my_room_dict["room_status"] = 999
    #print(f' my_room_dict["board"]["id"]: {my_room_dict["board"]["id"]}')
    print(f'Room1 board matrix: {my_room_dict["board"]["matrix"]}')
    assert my_room_dict["room_status"] == 999

    print("-----ROOM2-----------")
    print(type(room2.__dict__), room2.__dict__)
    print(f'Room2 board matrix: {my_room_dict["board"]["matrix"]}')
    assert room2.__dict__["room_status"] == 2

    return 0

if __name__ == "__main__":
    if db_models_test() == 0:
        print("db_models_test passed")
    else:
        print("db_models_test failed")

