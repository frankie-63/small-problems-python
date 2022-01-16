def output_decor(func_2):
    def wrap_o(*args, **kwargs):
        print("The result is:")
        func_2(*args, **kwargs)
    return wrap_o
