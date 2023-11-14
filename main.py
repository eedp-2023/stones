from circum_plot import points
from circumference import get_circumference
from Estimated_and_Exact_Area import Area_Calc


x0_loop_bool = True

while x0_loop_bool:
    user_x0_input = input("Welcome to The Stone team's Monte Carlo machine! " +
                          "Please enter the x0 coordinate of the origin of the circle: ")

    try:
        user_x0_input = float(user_x0_input)
        x0_loop_bool = False
        y0_loop_bool = True

        while y0_loop_bool:
            user_y0_input = input("Please enter the y0 coordinate of the origin of the circle: ")

            try:
                user_y0_input = float(user_y0_input)
                y0_loop_bool = False
                r_loop_bool = True

                while r_loop_bool:
                    user_r_input = input("Please enter the radius of the circle: ")

                    try:
                        user_r_input = float(user_r_input)

                        if user_r_input > 0:
                            r_loop_bool = False
                            N_loop_bool = True

                        else:
                            print("Please enter a positive number.")
                            continue

                        while N_loop_bool:
                            user_N_input = input("Please enter the number of points you would like on the circle: ")

                            try:
                                user_N_input = int(user_N_input)

                                if user_N_input > 0:
                                    N_loop_bool = False
                                    spacing_loop_bool = True

                                else:
                                    print("The value of N must be greater than 0.")
                                    continue

                                while spacing_loop_bool:
                                    user_spacing_input = input("Please enter 1 for equally spaced points or 2 for randomly spaced points: ")

                                    try:
                                        user_spacing_input = int(user_spacing_input)

                                        if user_spacing_input == 1 or user_spacing_input == 2:
                                            spacing_loop_bool = False

                                            print("Your inputs: ")
                                            print("Circle coordinates: (" + str(user_x0_input) + "," + str(user_y0_input) + ")")
                                            print("Radius: " + str(user_r_input))
                                            print("Number of points on circle: " + str(user_N_input))

                                            if user_spacing_input == 1:
                                                print("Spacing: equal")
                                            else:
                                                print("Spacing: random")

                                            print("\nCalculating circle parameters...\n")

                                            x_pts, y_pts = points(user_x0_input, user_y0_input, user_r_input,
                                                                  user_N_input, user_spacing_input)
                                            next_neighbor_dist, est_circumference, calc_circumference = get_circumference(x_pts, y_pts,
                                                                                                                          user_r_input, user_x0_input, user_y0_input)
                                            est_area, calc_area = Area_Calc(user_r_input, next_neighbor_dist)

                                            print("\nYour outputs: ")
                                            print(f"Estimated circumference: {est_circumference:.3f} units")
                                            print(f"Actual circumference: {calc_circumference:.3f} units")
                                            print(f"Estimated area: {est_area:.3f} units^2")
                                            print(f"Actual area: {calc_area:.3f} units^2")

                                        else:
                                            print("Please type either 1 or 2.")
                                    except:
                                        print("Please enter a number.")
                            except:
                                print("Please enter a positive, integer number.")
                    except:
                        print("Please enter a positive number.")
            except:
                print("Please enter a number.")
    except:
        print("Please enter a number.")