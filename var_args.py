""" var args demo """
def var_args(name, *args):
    print(name)
    print(args)

def var_args_with_keys(name, **kwargs):
    print(name)
    print(kwargs["desc"],kwargs["params"])

var_args("ram","aaaa","var args","one more")

var_args_with_keys("ram", desc="aaaa", params="var args",extra = "one more")