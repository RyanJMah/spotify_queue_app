import os
import sys
import time
# import multiprocessing as mp

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(THIS_DIR, "web"))

from web.app import app


def main():
	app.run(debug = True, host = "0.0.0.0", port = 80)

if __name__ == "__main__":
	main()
