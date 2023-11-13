x0_loop_bool = True
while x0_loop_bool:
    user_x0_input = input("Welcome to The Stone team's Monte Carlo machine! " +
                          "Please enter the x0 coordinate of the origin of the circle: ")
    try:
        user_x0_input = int(user_x0_input)
        x0_loop_bool = False
        y0_loop_bool = True
        while y0_loop_bool:
            user_y0_input = input("Please enter the y0 coordinate of the origin of the circle: ")
            try:
                user_y0_input = int(user_y0_input)
                y0_loop_bool = False
                r_loop_bool = True
                while r_loop_bool:
                    user_r_input = input("Please enter the radius of the circle: ")
                    try:
                        user_r_input = int(user_r_input)
                        r_loop_bool = False
                        N_loop_bool = True
                        while N_loop_bool:
                            user_N_input = input("Please enter the number of points you would like on the circle: ")
                            try:
                                user_N_input = float(user_N_input)
                                whole_num_verification = user_N_input.is_integer()
                                if not whole_num_verification:
                                    print("The value of N needs to be a whole number")
                                elif whole_num_verification:
                                    N_loop_bool = False
                                    spacing_loop_bool = True
                                    while spacing_loop_bool:
                                        user_spacing_input = input("Please enter 1 for equally spaced points or 2 for randomly spaced points: ")
                                        try:
                                            user_spacing_input = int(user_spacing_input)
                                            if user_spacing_input == 1 or user_spacing_input == 2:
                                                spacing_loop_bool = False
                                                if user_spacing_input == 1:
                                                    user_spacing_input = "equal"
                                                elif user_spacing_input == 2:
                                                    user_spacing_input = "random"
                                                print("Your inputs: ")
                                                print("Circle coordinates: (" + str(user_x0_input) + "," + str(user_y0_input) + ")")
                                                print("Radius: " + str(user_r_input))
                                                print("Number of points on circle: " + str(user_N_input))
                                                print("Spacing: " + str(user_spacing_input))
                                            else:
                                                print("Please type either 1 or 2")
                                        except:
                                            print("Please enter a number")
                            except:
                                print("Please enter a number")
                    except:
                        print("please enter a number")
            except:
                print("Please enter a number")
    except:
        print("Please enter a number")