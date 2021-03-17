{
 "metadata": {
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
   "version": "3.7.3-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.7.3 64-bit (conda)",
   "metadata": {
    "interpreter": {
     "hash": "0c6307be93a20823dc89b973f9d3a093429e258f117cb98268f635676c856dc8"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[6, 4, 5, 8, 7]\n"
     ]
    }
   ],
   "source": [
    "def reverse(arr):\n",
    "    arr.reverse()\n",
    "    return arr\n",
    "\n",
    "\n",
    "n = int(input())\n",
    "arr = []\n",
    "for i in range(0,n):\n",
    "    ele = int(input())\n",
    "    arr.append(ele)\n",
    "print(reverse(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-11-9c0d52c16399>, line 9)",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-11-9c0d52c16399>\"\u001b[1;36m, line \u001b[1;32m9\u001b[0m\n\u001b[1;33m    low ++\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# def rev(arr):\n",
    "#     low = 0\n",
    "#     n = len(arr)\n",
    "#     high = n - 1\n",
    "#     if(arr[low] < arr[high]):\n",
    "#         temp = arr[low]\n",
    "#         arr[low] = arr[high]\n",
    "#         arr[high] = temp\n",
    "#         low ++\n",
    "#         high --\n",
    "#         return arr\n",
    "\n",
    "# n = int(input())\n",
    "# arr = []\n",
    "# for i in range(0,n):\n",
    "#     ele = int(input())\n",
    "#     arr.append(ele)\n",
    "# print(reverse(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}