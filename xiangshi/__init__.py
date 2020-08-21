from xiangshi.main import calculator

calculator = calculator()
for x in dir(calculator):
    if x[:2] != "__":
        exec(x + "=" + "calculator." + x)
