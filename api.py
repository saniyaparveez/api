{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify, request, Response \n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    " app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "books = [\n",
    "\t{\n",
    "\t\t'name': 'A',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9780394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'B',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9792371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'C',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9800394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'D',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9812371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'E',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9820394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'F',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9832371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'G',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9840394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'H',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9852371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'I',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9860394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'K',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9872371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'L',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9880394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'M',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9892371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'N',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9900394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'O',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9912371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'P',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9920394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'Q',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9932371000193\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'R',\n",
    "\t\t'price': 7.99,\n",
    "\t\t'isbn': 9940394800165\n",
    "\t},\n",
    "\t{\n",
    "\t\t'name': 'S',\n",
    "\t\t'price': 6.99,\n",
    "\t\t'isbn': 9952371000193\n",
    "\t}\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/books\")\n",
    "def get_books():\n",
    "    books_data = jsonify({'books': books})\n",
    "    return books_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "app.run(port=5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
