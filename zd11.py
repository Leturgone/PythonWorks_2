class MillyError(Exception):
    pass

class MillyAutomaton:
    def __init__(self):
        self.state = 'A'
    
    
    def apply(self):
        if self.state == 'A':
            self.state = 'B'
            return 0;
        elif self.state == 'B':
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MillyError("apply")
    
    
    def align(self):
            if self.state == 'A':
                self.state = 'C'
                return 1
            elif self.state == 'B':
                self.state = 'C'
                return 2
            elif self.state == 'C':
                self.state = 'D'
                return 4
            elif self.state == 'D':
                self.state = 'B'
                return 6
            elif self.state == 'E':
                self.state = 'F'
                return 7
            elif self.state == 'F':
                self.state = 'A'
                return 9
            else:
                raise MillyError("align")
def main():
    return MillyAutomaton()

def raises(fun,error):
    output = None
    try:
        output = fun()
    except Exception as e:
        assert type(e) == error
    assert output is None
    
def test():
    o = main()
    assert o.apply() == 0
    assert o.apply() == 3
    assert o.align() == 2
    assert o.align() == 4
    assert o.apply() == 5
    assert o.align() == 7
    assert o.align() == 9
    assert o.align() == 1
    assert o.align() == 4
    assert o.align() == 6
    raises(o.apply, MillyError)

    o = main()
    assert o.apply() == 0
    assert o.align() == 1
    assert o.align() == 4
    assert o.align() == 6
    assert o.align() == 2
    assert o.align() == 4
    assert o.apply() == 5
    assert o.align() == 7
    assert o.align() == 9
    assert o.align() == 1
    assert o.align() == 4
    assert o.apply() == 5
    assert o.align() == 7
    assert o.apply() == 8
    raises(o.apply, MillyError)

test()

            
            
        