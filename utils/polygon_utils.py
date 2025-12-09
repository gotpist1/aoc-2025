class PolygonHelper:

    def is_rectangle_valid(self, left, right, top, bottom, polygon):
        """Check if all corners are inside/on polygon and no edges cross interior."""
        corners = [(left, top), (right, top), (left, bottom), (right, bottom)]
        for corner in corners:
            if not self.point_in_or_on_polygon(corner, polygon):
                return False

        center = ((left + right) / 2, (top + bottom) / 2)
        if not self.point_in_polygon_winding(center, polygon):
            return False

        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]

            if self.edge_on_rectangle_boundary(x1, y1, x2, y2, left, right, top, bottom):
                continue

            if self.edge_crosses_rectangle(x1, y1, x2, y2, left, right, top, bottom):
                return False

        return True


    def point_in_or_on_polygon(self, point, polygon):
        x, y = point

        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]

            if x1 == x2:
                if x == x1 and min(y1, y2) <= y <= max(y1, y2):
                    return True
            else:
                if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                    return True

        return self.point_in_polygon_winding(point, polygon)


    def point_in_polygon_winding(self, point, polygon):
        x, y = point
        winding_number = 0

        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]

            if y1 <= y:
                if y2 > y:
                    if self.is_left(x1, y1, x2, y2, x, y) > 0:
                        winding_number += 1
            else:
                if y2 <= y:
                    if self.is_left(x1, y1, x2, y2, x, y) < 0:
                        winding_number -= 1

        return winding_number != 0

    @staticmethod
    def is_left(x1, y1, x2, y2, px, py):
        return ((x2 - x1) * (py - y1) - (px - x1) * (y2 - y1))

    @staticmethod
    def edge_on_rectangle_boundary(x1, y1, x2, y2, left, right, top, bottom):
        if x1 == x2 == left and min(y1, y2) >= top and max(y1, y2) <= bottom:
            return True
        if x1 == x2 == right and min(y1, y2) >= top and max(y1, y2) <= bottom:
            return True
        if y1 == y2 == top and min(x1, x2) >= left and max(x1, x2) <= right:
            return True
        if y1 == y2 == bottom and min(x1, x2) >= left and max(x1, x2) <= right:
            return True
        return False

    def edge_crosses_rectangle(self, x1, y1, x2, y2, left, right, top, bottom):
        if max(x1, x2) < left or min(x1, x2) > right:
            return False
        if max(y1, y2) < top or min(y1, y2) > bottom:
            return False
        if x1 < left and x2 < left:
            return False
        if x1 > right and x2 > right:
            return False
        if y1 < top and y2 < top:
            return False
        if y1 > bottom and y2 > bottom:
            return False

        r_edges = [
            (left, top, right, top),
            (left, bottom, right, bottom),
            (left, top, left, bottom),
            (right, top, right, bottom)
        ]

        for rx1, ry1, rx2, ry2 in r_edges:
            if self.segments_intersect_properly(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
                return True

        return False

    @staticmethod
    def segments_intersect_properly(x1, y1, x2, y2, x3, y3, x4, y4):
        def ccw(ax, ay, bx, by, cx, cy):
            return (cy - ay) * (bx - ax) - (by - ay) * (cx - ax)

        d1 = ccw(x3, y3, x4, y4, x1, y1)
        d2 = ccw(x3, y3, x4, y4, x2, y2)
        d3 = ccw(x1, y1, x2, y2, x3, y3)
        d4 = ccw(x1, y1, x2, y2, x4, y4)

        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
                ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
            return True

        return False
