#  Generate random IDs from auto-generated unique IDs.
For instance: you maybe want to generate 1000 random user ids from 10 unique ids.
How it works: it generate random number in specific range and hash this number using md5 and convert it to hexdigest

## Usage:
-> initialize object that randomizes from 1M unique ID  
`random_ids_generator = RandomIdsGenerator(1000000)`  
  
-> generate list of 1 Million random ID (it takes -> 0.9 second ;) )   
`random_ids = random_ids_generator.randoms(1000000)`  
  
-> generate a single random ID  
`random_id = random_ids_generator.random()` 
   
-> get the unique IDs  
`unique_ids = random_ids_generator.get_unique_ids()`  
