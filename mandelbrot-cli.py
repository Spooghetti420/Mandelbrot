import argparse
import sys
from io import BytesIO
from mandelbrot import render_mandelbrot

def main():
    parser = argparse.ArgumentParser(description="Render the Mandelbrot set given various parameters.")
    parser.add_argument("width", type=int, nargs=1,
                    help="width of the output image")
    parser.add_argument("height", type=int, nargs=1,
                    help="height of the output image")

    parser.add_argument("--zoom", "-Z", dest="zoom", type=float, nargs=1, default=[1.0],
                    help="factor by which to magnify the image, thus zooming into the fractal")
    
    parser.add_argument("--x-offset", "--dx", dest="dx", type=float, nargs=1, default=[0.0],
                    help="x-value by which to move before rendering the graph")
    
    parser.add_argument("--y-offset", "--dy", dest="dy", type=float, nargs=1, default=[0.0],
                    help="y-value by which to move before rendering the graph")

    parser.add_argument("--iterations", "-I", dest="iterations", type=int, nargs=1, default=[100],
                    help="maximum of iterations to perform per pixel")

    parser.add_argument("--threshold", "-T", dest="threshold", type=float, nargs=1, default=[16.0],
                    help="maximum absolute value (squared) that each pixel can reach before being considered divergent")

    parser.add_argument("--show-only", "-S", dest="show_only", action="store_true",
                    help="do not output the image, but simply display it in a separate window")

    args = parser.parse_args()
    
    width = args.width[0]
    height = args.height[0] if args.height else width
    zoom = args.zoom[0]
    dx = args.dx[0]
    dy = args.dy[0]
    iterations = args.iterations[0]
    threshold = args.threshold[0]

    render = render_mandelbrot(width, height, dx, dy, zoom, iterations, threshold)

    if args.show_only:
        render.show()
    else:
        buffer = BytesIO()
        render.save(buffer, "PNG")
        sys.stdout.buffer.write(buffer.getvalue())

if __name__ == "__main__":
    main()