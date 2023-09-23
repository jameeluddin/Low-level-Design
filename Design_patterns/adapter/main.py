from Design_patterns.adapter.circle import Circle
from Design_patterns.adapter.draw_service import DrawService
from Design_patterns.adapter.square import Square


def main():
    draw_service = DrawService()
    draw_service.add_shapes(Square())
    draw_service.add_shapes(Circle())

    draw_service.draw()
    draw_service.resize()


if __name__ == "__main__":
    main()
