#!/bin/bash
cd ~/oscar-dev/backend
source venv/bin/activate
uvicorn main:app --reload
