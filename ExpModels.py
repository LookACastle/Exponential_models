GlowScript 2.2 VPython

temp_data = [15, 16, 18, 19, 22, 24, 31, 42, 49, 67, 78, 90, 105, 109, 122, 125]

# Makes the big black box disappear
scene.width = 0
scene.height = 0

def get_projection_factor(list):
    output = []
    for i in range(len(list) - 1):
        projection_factor = 100 / list[i] * list[i + 1] / 100
        output.append(projection_factor)
    return output

def graph_func(logarithmic):
    g = graph(logy = logarithmic.checked, width = 600, height = 600, xmin = 0, ymin = 0)

    points = gdots(color = color.blue)

    for x in range(len(temp_data)):
        points.plot(x, temp_data[x])


checkbox(bind = graph_func, text = "Logarithmic toggle")
