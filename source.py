class ParamTypeAssertion(object):
    
    # The parameters of the decorator go into here
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    # the function "object" is plugged into here
    def __call__(self, function):
        
        # Wrap the function with a wrapper
        def wrapper(*args, **kwargs):
            # check if input is same length as 
            if len(args) != len(self.args):
                raise ValueError("Invalid TypeHeader")
            
            # check if all args are acceptable types
            for i, x in enumerate(args):
                if type(self.args[i]) == list and (type(args[i]) not in self.args[i]):
                    raise TypeError("Invalid Type: Recieved:", args[i], "Expecting types:", self.args[i])
                elif type(self.args[i]) != list and (type(args[i]) != self.args[i]):
                    raise TypeError("Invalid Type: Recieved:", args[i], "Expecting type:", self.args[i])
                    
            # check if all kwargs are acceptable types
            for i, x in kwargs.items():
                if type(self.kwargs[i]) == list and (type(kwargs[i]) not in self.kwargs[i]):
                    raise TypeError("Invalid Type: Recieved:", kwargs[i], "Expecting types:", self.kwargs[i])
                elif type(self.kwargs[i]) != list and (type(kwargs[i]) != self.kwargs[i]):
                    raise TypeError("Invalid Type: Recieved:", kwargs[i], "Expecting type:", self.kwargs[i])
            
            # if all checks out, return the function
            return function(*args, **kwargs)
        
        # return the wrapper
        return wrapper


class ReturnTypeAssertion():
    
    # The parameters of the decorator go into here
    def __init__(self, returnType):
        self.returnTypes = returnType
    
    # the function "object" goes in here
    def __call__(self, function):
        
        # the wrapper function
        def wrapper(*args, **kwargs):
            
            # get the function return value
            value = function(*args, **kwargs)
            
            # check the type of the value
            if type(value) == self.returnTypes or type(self.args) == list and type(value) in self.returnTypes:
                return value
            
            # otherwise, raise ValueError
            raise ValueError("Invalid Return type")
        
        # return the wrapper
        return wrapper
        
if __name__ == "__main__":        
    @ReturnTypeAssertion([str, float])
    @ParamTypeAssertion(list, [str, float], [object, float, bool])
    def test(x, y, z):
        print(x, y, z)
        return "test"
