{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "07d5d5a0-f7f2-46f0-afaa-682db10b193d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'key1': 404,\n",
       " 'key2': '2',\n",
       " 'key3': [3, 3, 3],\n",
       " 'key4': (4, 4, 4),\n",
       " 'key5': 5,\n",
       " (0, 1): 6}"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create the dictionary\n",
    "\n",
    "Dict = {\"key1\": 404, \"key2\": \"2\", \"key3\": [3, 3, 3], \"key4\": (4, 4, 4), ('key5'): 5, (0, 1): 6}\n",
    "Dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "948cf79e-1d9f-4be6-9b85-339b3a5b6ef0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "404"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Access to the value by the key\n",
    "Dict[\"key1\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1df8fc36-0b41-4937-94bf-e6bbba4bb29b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Thriller': '1982',\n",
       " 'Back in Black': '1980',\n",
       " 'The Dark Side of the Moon': '1973',\n",
       " 'The Bodyguard': '1992',\n",
       " 'Bat Out of Hell': '1977',\n",
       " 'Their Greatest Hits (1971-1975)': '1976',\n",
       " 'Saturday Night Fever': '1977',\n",
       " 'Rumours': '1977',\n",
       " 'Viva la Vida or Death and All His Friends': '2008'}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a sample dictionary\n",
    "\n",
    "release_year_dict = {\"Thriller\": \"1982\", \"Back in Black\": \"1980\", \\\n",
    "                    \"The Dark Side of the Moon\": \"1973\", \"The Bodyguard\": \"1992\", \\\n",
    "                    \"Bat Out of Hell\": \"1977\", \"Their Greatest Hits (1971-1975)\": \"1976\", \\\n",
    "                    \"Saturday Night Fever\": \"1977\", \"Rumours\": \"1977\", \"Viva la Vida or Death and All His Friends\": \"2008\"}\n",
    "release_year_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b6d014f5-938e-411b-8105-2b535723cbf0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2008'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get value by keys - retrieve the values based on the names:\n",
    "release_year_dict['Viva la Vida or Death and All His Friends'] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b96bbf2a-c88d-4837-980b-bf31a348c869",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours', 'Viva la Vida or Death and All His Friends'])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get all the keys in dictionary - retrieve the keys of the dictionary using the method keys():\n",
    "\n",
    "release_year_dict.keys() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "608f26e4-52dc-4d37-9c9e-36452c51cbf7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Thriller': '1982',\n",
       " 'Back in Black': '1980',\n",
       " 'The Dark Side of the Moon': '1973',\n",
       " 'The Bodyguard': '1992',\n",
       " 'Bat Out of Hell': '1977',\n",
       " 'Their Greatest Hits (1971-1975)': '1976',\n",
       " 'Saturday Night Fever': '1977',\n",
       " 'Rumours': '1977',\n",
       " 'Viva la Vida or Death and All His Friends': '2008',\n",
       " 'Graduation': '2007',\n",
       " 'X&Y': '2005'}"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Append value with key into dictionary\n",
    "\n",
    "release_year_dict['X&Y'] = '2005'\n",
    "release_year_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c23f7a13-5b4e-4c8a-8b27-3b1991a7f252",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Verify the key is in the dictionary - verify if an element is in the dictionary:\n",
    "'Rumours' in release_year_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "01192453-1643-4fb3-80a5-d0a81f150900",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Verify the key is in the dictionary - verify if an element is in the dictionary:\n",
    "'Parachutes' in release_year_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5ed75a0e-4ebf-4037-8d87-935502c4772c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Tubular Bells': '1973',\n",
       " 'Hergest Ridge': '1974',\n",
       " 'Ommadawn': '1975',\n",
       " 'Incantations': '1978',\n",
       " 'Platinum': '1979',\n",
       " 'QE2': '1980',\n",
       " 'Five Miles Out': '1982',\n",
       " 'Crises': '1983'}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Question sample dictionary\n",
    "\n",
    "soundtrack_dic = {\"Tubular Bells\": \"1973\", \"Hergest Ridge\": \"1974\", \"Ommadawn\": \"1975\", \"Incantations\": \"1978\", \"Platinum\": \"1979\", \\\n",
    "                  \"QE2\": \"1980\", \"Five Miles Out\": \"1982\", \"Crises\": \"1983\"}\n",
    "soundtrack_dic "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6bdd6ac0-0ee9-44d7-92e4-0cdef489533b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['Tubular Bells', 'Hergest Ridge', 'Ommadawn', 'Incantations', 'Platinum', 'QE2', 'Five Miles Out', 'Crises'])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#In the dictionary soundtrack_dic what are the keys ? - Get all the keys in dictionary\n",
    "soundtrack_dic.keys() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "036c5754-f9e1-442d-aa45-58f7adb7859f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['1973', '1974', '1975', '1978', '1979', '1980', '1982', '1983'])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#In the dictionary soundtrack_dic what are the values ? - Get all the values in dictionary\n",
    "soundtrack_dic.values() "
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
