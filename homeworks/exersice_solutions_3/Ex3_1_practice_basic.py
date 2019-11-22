NUM_1 = 10
NUM_2 = 2
BOOL_1 = True
BOOL_2 = False

if BOOL_1 is True:
    print("BOOL_1 is True")

if not BOOL_2:
    print("not BOOL_2")

if BOOL_2 is False and NUM_1 < NUM_2:
    print("BOOL_2 is False and NUM_1 < NUM_2")
elif NUM_1 < NUM_2:
    print("NUM_1 < NUM_2")
elif BOOL_2 is False:
    print("BOOL_2 is False")
else:
    print("Nothing satisfy!")

