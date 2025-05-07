#Part 2
linear_sum([A], 8)
    linear_sum([A], 7)
        linear_sum([A], 6)
            linear_sum([A], 5)
                linear_sum([A], 4)
                    linear_sum([A], 3)
                        linear_sum([A], 2)
                            linear_sum([A], 1)
                                linear_sum([A], 0)
                                    return A[0]
                                return A[1] + A[0]  
                            return A[2] + (A[1] + A[0])