import os
import subprocess
from mandelbrot import render_mandelbrot

os.makedirs("frames", exist_ok=True)
for frame in range(1, 97):
    print(f"Processing frame {frame}...", end=" ", flush=True)
    render_mandelbrot(600, 600, y_offset=-1, zoom=1.5**frame).save(os.path.join("frames", f"frame{frame:03}.png"))
    print("done")

subprocess.run(["ffmpeg", "-framerate", "24", "-i", "frame%03d.png", "mandelbrot.gif"], cwd="frames")