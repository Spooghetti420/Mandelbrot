import os
import subprocess
from mandelbrot import render_mandelbrot

os.makedirs("frames", exist_ok=True)
for zoom in range(1, 501):
    render_mandelbrot(600, 600, y_offset=-1, zoom=zoom).save(os.path.join("frames", f"frame{zoom:03}.png"))

subprocess.run(["ffmpeg", "-framerate", "24", "-i", "frame%03d.png", "mandelbrot.gif"], cwd="frames")