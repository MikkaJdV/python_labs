{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7052c34e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.1, 1982]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a list\n",
    "\n",
    "L = [\"Michael Jackson\", 10.1, 1982]\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "89f9ed23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the same element using negative and positive indexing:\n",
      " Postive: Michael Jackson \n",
      " Negative: Michael Jackson\n",
      "the same element using negative and positive indexing:\n",
      " Postive: 10.1 \n",
      " Negative: 10.1\n",
      "the same element using negative and positive indexing:\n",
      " Postive: 1982 \n",
      " Negative: 1982\n"
     ]
    }
   ],
   "source": [
    "# Print the elements on each index\n",
    "\n",
    "print('the same element using negative and positive indexing:\\n Postive:',L[0],\n",
    "'\\n Negative:' , L[-3]  )\n",
    "print('the same element using negative and positive indexing:\\n Postive:',L[1],\n",
    "'\\n Negative:' , L[-2]  )\n",
    "print('the same element using negative and positive indexing:\\n Postive:',L[2],\n",
    "'\\n Negative:' , L[-1]  )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "61df89ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1)]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Sample List\n",
    "\n",
    "[\"Michael Jackson\", 10.1, 1982, [1, 2], (\"A\", 1)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "97235820",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.1, 1982, 'MJ', 1]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Sample List\n",
    "\n",
    "L = [\"Michael Jackson\", 10.1,1982,\"MJ\",1]\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2c166d51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.1, 1982]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# List slicing\n",
    "\n",
    "L[0:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6a2c7cb6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.2, 'superstar', 777]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use extend to add elements to list\n",
    "\n",
    "L = [ \"Michael Jackson\", 10.2]\n",
    "L.extend(['superstar', 777])\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b5c409ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson', 10.2, ['superstar', 12]]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use append to add elements to list\n",
    "\n",
    "L = [ \"Michael Jackson\", 10.2]\n",
    "L.append(['superstar', 12])\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c3abd9e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before change: ['disco', 10, 1.2]\n",
      "After change: ['post rock', 77, 1.2]\n"
     ]
    }
   ],
   "source": [
    "# Change the element based on the index\n",
    "\n",
    "A = [\"disco\", 10, 1.2]\n",
    "print('Before change:', A)\n",
    "A[0] = 'post rock'\n",
    "A[1] = 77\n",
    "print('After change:', A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "71a0691d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Michael Jackson',\n",
       " 10.2,\n",
       " ['superstar', 12],\n",
       " ['a', 'b'],\n",
       " ['a', 'b'],\n",
       " ['c', 'd']]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use append to add elements to list\n",
    "\n",
    "L.append(['c','d'])\n",
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1d5dfb95",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before change: ['post rock', 77, 1.2]\n",
      "After change: [77, 1.2]\n"
     ]
    }
   ],
   "source": [
    "# Delete the element based on the index\n",
    "\n",
    "print('Before change:', A)\n",
    "del(A[0])\n",
    "print('After change:', A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2f2109a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Alexander', 'Pushkin']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Split the string, default is by space\n",
    "\n",
    "'Alexander Pushkin'.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2eaf4e6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['A', 'B', 'C', 'D']"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Split the string by comma\n",
    "\n",
    "'A;B;C;D'.split(';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8ad425c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A: ['hard rock', 10, 1.2]\n",
      "B: ['hard rock', 10, 1.2, 'dogs']\n"
     ]
    }
   ],
   "source": [
    "# Copy (copy by reference) the list A\n",
    "\n",
    "A = [\"hard rock\", 10, 1.2]\n",
    "A1= A +[\"dogs\"]\n",
    "B = A1\n",
    "print('A:', A)\n",
    "print('B:', B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45afcd2a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f968a11a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B[0]: hard rock\n",
      "B[0]: hard rock\n"
     ]
    }
   ],
   "source": [
    "# Examine the copy by reference\n",
    "\n",
    "print('B[0]:', B[0])\n",
    "A[0] = \"banana\"\n",
    "print('B[0]:', B[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b94c7bf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 'hello', [1, 2, 3], True]\n"
     ]
    }
   ],
   "source": [
    "a_list = [1, \"hello\", [1,2,3], True]\n",
    "print(a_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d94e8602",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the value stored at index 1 of a_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "fe22f546",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the same element using negative and positive indexing:\n",
      " Postive: 1 \n",
      " Negative: 1\n",
      "the same element using negative and positive indexing:\n",
      " Postive: hello \n",
      " Negative: hello\n",
      "the same element using negative and positive indexing:\n",
      " Postive: [1, 2, 3] \n",
      " Negative: [1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "print('the same element using negative and positive indexing:\\n Postive:',a_list[0],\n",
    "'\\n Negative:' , a_list[-4]  )\n",
    "print('the same element using negative and positive indexing:\\n Postive:',a_list[1],\n",
    "'\\n Negative:' , a_list[-3]  )\n",
    "print('the same element using negative and positive indexing:\\n Postive:',a_list[2],\n",
    "'\\n Negative:' , a_list[-2]  )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "d073df2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "print(a_list[-2][2])\n",
    "print(a_list[-2][1])\n",
    "print(a_list[-2][0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84479c68",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "c480515c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before change: [1, 'a']\n",
      "After change: [1, 'a', 2, 1, 'd']\n"
     ]
    }
   ],
   "source": [
    "A = [1, 'a']\n",
    "print('Before change:', A)\n",
    "B = [2, 1, 'd']\n",
    "A=A+B\n",
    "print('After change:' , A)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
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
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
