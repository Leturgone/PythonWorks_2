class MealyError(Exception):
    pass


class MillyAutomaton:
    state = "A"

    def apply(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            return 3
        elif self.state == "D":
            self.state = "E"
            return 5
        elif self.state == "F":
            self.state = "G"
            return 8
        else:
            raise (MealyError("apply"))

    def align(self):
        if self.state == "A":
            self.state = "C"
            return 1
        elif self.state == "B":
            self.state = "C"
            return 2
        elif self.state == "C":
            self.state = "D"
            return 4
        elif self.state == "D":
            self.state = "B"
            return 6
        elif self.state == "E":
            self.state = "F"
            return 7
        elif self.state == "F":
            self.state = "A"
            return 9
        else:
            raise MealyError("align")


def main():
    return MillyAutomaton()


def raises(fun, error):
    output = None
    try:
        output = fun()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    o.state = "G"
    raises(lambda: o.align(), MealyError)
    o = main()
    assert o.state == "A"
    assert o.apply() == 0
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.align() == 9
    assert o.state == "A"
    assert o.align() == 1
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.align() == 6

    o = main()
    assert o.state == "A"
    assert o.apply() == 0
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.align() == 9
    assert o.state == "A"
    assert o.align() == 1
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.align() == 6
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.apply() == 8
    assert o.state == "G"
    raises(lambda: o.apply(), MealyError)

    o = main()
    assert o.state == "A"
    assert o.align() == 1
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.align() == 6
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.apply() == 8
    assert o.state == "G"
    raises(lambda: o.apply(), MealyError)

    o = main()
    assert o.state == "A"
    assert o.align() == 1
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.align() == 9
    assert o.state == "A"
    assert o.apply() == 0
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.apply() == 8
    assert o.state == "G"
    raises(lambda: o.apply(), MealyError)

    o = main()
    assert o.state == "A"
    assert o.align() == 1
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.align() == 6
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.align() == 9
    assert o.state == "A"
    assert o.apply() == 0
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.apply() == 8
    assert o.state == "G"
    raises(lambda: o.apply(), MealyError)

    o = main()
    assert o.state == "A"
    assert o.apply() == 0
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.align() == 6
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.align() == 9
    assert o.state == "A"
    assert o.align() == 1
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.align() == 6
    assert o.state == "B"
    assert o.apply() == 3
    assert o.state == "B"
    assert o.align() == 2
    assert o.state == "C"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 4
    assert o.state == "D"
    assert o.apply() == 5
    assert o.state == "E"
    raises(lambda: o.apply(), MealyError)
    assert o.align() == 7
    assert o.state == "F"
    assert o.apply() == 8
    assert o.state == "G"
    raises(lambda: o.apply(), MealyError)
    
test()



# def test():
#     test_exeptions = [
#         ('C', 'apply'),
#         ('E', 'apply'),
#         ('G', 'apply'),
#         ('G', 'align')
#     ]
#     test_result = [
#         ('A', 'apply', 0, 'B'),
#         ('A', 'align', 1, 'C'),
#         ('B', 'align', 2, 'C'),
#         ('B', 'apply', 3, 'B'),
#         ('C', 'align', 4, 'D'),
#         ('D', 'apply', 5, 'E'),
#         ('D', 'align', 6, 'B'),
#         ('E', 'align', 7, 'F'),
#         ('F', 'apply', 8, 'G'),
#         ('F', 'align', 9, 'A')
#     ]
#     sm = main()
    
#     for start_state, action in test_exeptions:
#         sm.state = start_state
#         try:
#             if action == 'apply':
#                 sm.apply()
#             else:
#                 sm.align()
#         except MillyError:
#             pass
#     for start_state, action, expected_return, exepted_state in test_result:
#         sm.state = start_state
#         if action == 'apply':
#             assert sm.apply() == expected_return
#             assert sm.state == exepted_state
#         else:
#             assert sm.align() == expected_return
#             assert sm.state == exepted_state

# test()



            
            
        