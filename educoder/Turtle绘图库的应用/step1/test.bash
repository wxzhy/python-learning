#!/bin/bash
python3 step1/src.py
convert step1/sj.ps step1/sj.jpg
python3 step1/compare.py
