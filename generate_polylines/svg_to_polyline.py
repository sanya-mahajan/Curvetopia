from svgpathtools import svg2paths


paths, _ = svg2paths('output.svg')

polylines = []
for path in paths:
    polyline = []
    for segment in path:
        polyline.append(segment.start)
        polyline.append(segment.end)
    polylines.append(polyline)

# first polyline
print(polylines[0])
