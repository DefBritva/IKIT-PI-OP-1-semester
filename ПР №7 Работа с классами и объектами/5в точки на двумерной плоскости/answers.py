def get_answer(xy, constraint):
    """
    a function that will count whether a point is in a constraint
    """
    desired_points = []
    for i in range(0, len(xy)):
        if constraint.constr_x[0] <= int((xy[i])[0]) <= constraint.constr_x[1]\
            and constraint.constr_y[0] <= int((xy[i])[1]) <= constraint.constr_y[1]:
            desired_points.append(xy[i])
    print('points satisfying the constraints', desired_points)
    return desired_points
