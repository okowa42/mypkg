import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")


def cb(request, response):
    if request.name == "廣原灯":
        response.age = 21
    else:
        response.age = 255

    return response


def main():
    srv = node.create_service(Query, "Query", cb)
    rclpy.spin(node)
